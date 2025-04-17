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


def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
    conn.commit()
    print("Inserted successfully.")


def insert_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            if len(row) >= 2:
                cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("CSV data inserted successfully.")


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


def delete_user(username=None, phone=None):
    if username:
        cur.execute("DELETE FROM phonebook WHERE username = %s", (username,))
    elif phone:
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()
    print("Delete successful.")


def main():
    create_table()

    while True:
        
        print("1. Insert from console")
        print("2. Insert from CSV")
        print("3. Update user")
        print("4. Query data")
        print("5. Delete user")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            path = input("Enter CSV file path: ")
            insert_from_csv(path)
        elif choice == '3':
            old = input("Enter current username: ")
            new_name = input("Enter new username (or press Enter to skip): ")
            new_phone = input("Enter new phone (or press Enter to skip): ")
            update_user(old_username=old, new_username=new_name if new_name else None, new_phone=new_phone if new_phone else None)
        elif choice == '4':
            filter_name = input("Search by username (or press Enter to show all): ")
            filter_phone = input("Search by phone (or press Enter to skip): ")
            query_data(username=filter_name if filter_name else None, phone=filter_phone if filter_phone else None)
        elif choice == '5':
            del_name = input("Enter username to delete (or press Enter to skip): ")
            del_phone = input("Enter phone to delete (or press Enter to skip): ")
            delete_user(username=del_name if del_name else None, phone=del_phone if del_phone else None)
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
