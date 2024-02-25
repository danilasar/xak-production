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

    #def join_course(self, ):

    def is_course_member(self, user_id, course_id)->bool:
        result = self.cursor.execute("SELECT id FROM course_members WHERE user_id = ? AND course_id = ?", (user_id,course_id))
        return bool(len(result.fetchall()))

    def getTask(self, task_id):
        result = self.cursor.execute("SELECT * FROM tasks WHERE task_id = ?", (task_id))
        return result.fetchall()

    def add_solve(self, user_id, task_id):
        result = self.cursor.execute("INSERT INTO task_solutions (user_id, task_id) VALUES (%s, %s)", (user_id, task_id))
        self.conn.commit()

    def get_last_attempt(self, solution_id):
        result = self.cursor.execute("SELECT * FROM attempts WHERE solution_id=? ORDER B", (solution_id))
        self.conn.commit()
    def add_attempt(self, solution_id, commit_id):
        result = self.cursor.execute("INSERT INTO attempts (solution_id, commit_id) VALUES (%s, %s)", (solution_id, commit_id))
        self.conn.commit()

'''
    def delete_user(self, username):
        id = self.get_user_id(username)
        self.cursor.execute("DELETE FROM users WHERE id = ?", (id,))
        self.cursor.execute("DELETE FROM user_data WHERE users_id = ?", (id,))
        self.conn.commit()
'''