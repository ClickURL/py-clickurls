import psycopg2 as db
from config import settings
from models.model_user import User

class Database:
    
    def __init__(self):
        self.url = settings.database_url
    
    def get_user(self, user_id):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor()
                sql_statements = "SELECT * FROM users WHERE user_id = %s"
                data = [user_id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                cursor.close()
                return result
        except Exception as err:
            print("Get User DB Error: ", err)
    
    def get_users(self):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor()
                sql_statements = "SELECT * FROM users WHERE deleted_at IS NULL"
                cursor.execute(sql_statements)
                result = cursor.fetchall()
                cursor.close()
                return result
        except Exception as err:
            print("Get Users Error: ", err)

    def create_user(self, user_name):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor()
                sql_statements = "INSERT INTO users (username) VALUES (%s) RETURNING *"
                data = [user_name]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                cursor.close()
                return result
        except Exception as err:
            print("Create User Error: ", err)

    def update_user(self, user_name, user_updated_at, user_id):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor()
                sql_statements = "UPDATE users SET username = %s, updated_at = %s WHERE user_id = %s RETURNING *"
                data = [user_name, user_updated_at, user_id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                cursor.close()
                return result
        except Exception as err:
            print("Update User Error: ", err)

    def delete_user(self, user_id, user_delete_at):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor()
                sql_statements = "UPDATE users SET deleted_at = %s WHERE user_id = %s RETURNING *"
                data = [user_delete_at , user_id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                cursor.close()
                return result
        except Exception as err:
            print("Delete User Error: ", err)
