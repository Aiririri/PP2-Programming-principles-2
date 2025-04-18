import psycopg2

def connect_db():
    conn = psycopg2.connect(
        dbname="snake_db",
        user="postgres",
        password="27112005a",
        host="localhost",
        port="5432"
    )
    return conn, conn.cursor()

def get_or_create_user(cur, conn, username):
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        return user[0]
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    return user_id

def get_last_score(cur, user_id):
    cur.execute("SELECT score, level FROM user_scores WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1", (user_id,))
    return cur.fetchone()

def save_game_state(cur, conn, user_id, score, level):
    cur.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
    conn.commit()
