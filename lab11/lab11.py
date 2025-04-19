import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",    
    user="postgres",      
    password="27112005a"    
)
cur = conn.cursor()

def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    """)
    conn.commit()


def setup_sql_functions_and_procedures():
    cur.execute("""
        CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
        RETURNS TABLE(id INT, username TEXT, phone TEXT) AS $$
        BEGIN
            RETURN QUERY
            SELECT * FROM phonebook
            WHERE username ILIKE '%' || pattern || '%'
               OR phone ILIKE '%' || pattern || '%';
        END;
        $$ LANGUAGE plpgsql;
    """)

    cur.execute("""
        CREATE OR REPLACE PROCEDURE insert_or_update_user(p_username TEXT, p_phone TEXT)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            IF EXISTS (SELECT 1 FROM phonebook WHERE username = p_username) THEN
                UPDATE phonebook SET phone = p_phone WHERE username = p_username;
            ELSE
                INSERT INTO phonebook(username, phone) VALUES (p_username, p_phone);
            END IF;
        END;
        $$;
    """)

    cur.execute("""
        CREATE OR REPLACE PROCEDURE insert_many_users(
            IN names TEXT[],
            IN phones TEXT[],
            OUT invalid_entries TEXT[]
        )
        LANGUAGE plpgsql
        AS $$
        DECLARE
            i INT;
        BEGIN
            invalid_entries := ARRAY[]::TEXT[];
            FOR i IN 1..array_length(names, 1) LOOP
                IF phones[i] ~ '^\\d{6,15}$' THEN
                    CALL insert_or_update_user(names[i], phones[i]);
                ELSE
                    invalid_entries := array_append(invalid_entries, names[i] || ':' || phones[i]);
                END IF;
            END LOOP;
        END;
        $$;
    """)

    cur.execute("""
        CREATE OR REPLACE FUNCTION get_paginated_data(p_limit INT, p_offset INT)
        RETURNS TABLE(id INT, username TEXT, phone TEXT) AS $$
        BEGIN
            RETURN QUERY
            SELECT * FROM phonebook
            ORDER BY id
            LIMIT p_limit OFFSET p_offset;
        END;
        $$ LANGUAGE plpgsql;
    """)

    cur.execute("""
        CREATE OR REPLACE PROCEDURE delete_user(p_username TEXT, p_phone TEXT)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            IF p_username IS NOT NULL THEN
                DELETE FROM phonebook WHERE username = p_username;
            ELSIF p_phone IS NOT NULL THEN
                DELETE FROM phonebook WHERE phone = p_phone;
            END IF;
        END;
        $$;
    """)

    conn.commit()


def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone: ")
    cur.execute("CALL insert_or_update_user(%s, %s)", (username, phone))
    conn.commit()
    print("Inserted or updated successfully.")

def insert_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        names, phones = [], []
        for row in reader:
            if len(row) >= 2:
                names.append(row[0])
                phones.append(row[1])
        cur.execute("CALL insert_many_users(%s, %s, NULL)", (names, phones))
        conn.commit()
        print("CSV data processed.")

def update_user(old_username=None, new_username=None, new_phone=None):
    if old_username:
        if new_username:
            cur.execute("UPDATE phonebook SET username = %s WHERE username = %s", (new_username, old_username))
        if new_phone:
            cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (new_phone, old_username))
        conn.commit()
        print("Update successful.")

def query_data(username=None, phone=None):
    if username:
        cur.execute("SELECT * FROM phonebook WHERE username = %s", (username,))
    elif phone:
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    else:
        cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    print("Results:")
    for row in rows:
        print(row)

def search_by_pattern(pattern):
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    print("Pattern Results:")
    for row in rows:
        print(row)

def paginated_query(limit, offset):
    cur.execute("SELECT * FROM get_paginated_data(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_user(username=None, phone=None):
    cur.execute("CALL delete_user(%s, %s)", (username, phone))
    conn.commit()
    print("Delete successful.")

def main():
    create_table()
    setup_sql_functions_and_procedures()

    while True:
        print("\n1. Insert from console")
        print("2. Insert from CSV")
        print("3. Update user")
        print("4. Query data")
        print("5. Search by pattern")
        print("6. Paginated query")
        print("7. Delete user")
        print("8. Exit")            

        choice = input("Enter choice (1-8): ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            path = input("Enter CSV file path: ")
            insert_from_csv(path)
        elif choice == '3':
            old = input("Enter current username: ")
            new_name = input("Enter new username: ")
            new_phone = input("Enter new phone : ")
            update_user(old_username=old, new_username=new_name if new_name else None, new_phone=new_phone if new_phone else None)
        elif choice == '4':
            filter_name = input("Search by username: ")
            filter_phone = input("Search by phone ")
            query_data(username=filter_name if filter_name else None, phone=filter_phone if filter_phone else None)
        elif choice == '5':
            pattern = input("Enter search pattern: ")
            search_by_pattern(pattern)
        elif choice == '6':
            limit = int(input("Enter limit: "))
            offset = int(input("Enter offset: "))
            paginated_query(limit, offset)
        elif choice == '7':
            del_name = input("Enter username to delete: ")
            del_phone = input("Enter phone to delete : ")
            delete_user(username=del_name if del_name else None, phone=del_phone if del_phone else None)
        elif choice == '8':
            break
        else:
            print("Error")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
