import psycopg2
from config import DB_HOST, DB_PORT, DB_USER, DB_NAME, DB_PASS

class MyDataBase:

    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        result = self.cursor.execute("SELECT id FROM users WHERE user_id = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, username):
        result = self.cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        return result.fetchone()[0]

    def add_course(self, owner_id, category, name, is_open, sword):
        self.cursor.execute("INSERT INTO courses (owner_id, category, name, is_open, sword) VALUES (%s, %s, %s, %s, %s)", (owner_id, category, name, bool(is_open), sword))
        self.conn.commit()

    def add_group(self, owner_id, members_id, name):
        self.cursor.execute("INSERT INTO groups VALUES (%s, %s)", (owner_id, name))
        self.conn.commit()
        q = self.cursor.execute("SELECT id FROM groups WHERE name LIKE %s", (name,))
        for members in members_id:
            self.cursor.execute("INSERT INTO group VALUES (%s)", (q, members))
        self.conn.commit()

    #def join_course(self, ):

'''
    def delete_user(self, username):
        id = self.get_user_id(username)
        self.cursor.execute("DELETE FROM users WHERE id = ?", (id,))
        self.cursor.execute("DELETE FROM user_data WHERE users_id = ?", (id,))
        self.conn.commit()
'''