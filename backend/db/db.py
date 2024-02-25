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
        return "Course added in db"

    def add_group(self, owner_id, members_id, name):
        self.cursor.execute("INSERT INTO groups (owner_id, name) VALUES (%s, %s)", (owner_id, name))
        self.conn.commit()
        print(name)
        created_course = self.cursor.execute("SELECT id FROM groups WHERE name LIKE %s", (name,))
        print(created_course)
        created_course_id = created_course.fetchone()[0]
        for members in members_id:
            self.cursor.execute("INSERT INTO group_members VALUES (%s, %s)", (created_course_id, members))
        self.conn.commit()
        return "Group added in db"

    def join_course(self, user_id, role_id, course_id):
        self.cursor.execute("INSERT INTO course_members VALUES (%s, %s, %s)", (user_id, role_id, course_id))
        self.conn.commit()
        return f"User with ID {user_id} assigned to course {course_id}!"

    def create_task(self, course_id, name, max_grade, description):
        self.cursor.execute("INSERT INTO tasks (course_id, name, max_grade, description) VALUES (%s, %s, %s, %s)", (course_id, name, max_grade, description))
        self.conn.commit()
        return f"Task {name} added to course with ID {course_id}"
'''
    def delete_user(self, username):
        id = self.get_user_id(username)
        self.cursor.execute("DELETE FROM users WHERE id = ?", (id,))
        self.cursor.execute("DELETE FROM user_data WHERE users_id = ?", (id,))
        self.conn.commit()
'''