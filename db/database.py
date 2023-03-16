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
                if not result:
                  return None
                user_return = User(result[1], result[0], result[2], result[3], result[4])
                return user_return
        except Exception as err:
            print("Get User Error: ", err) 
        return None
    
    def get_users(self):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor()
                sql_statements = "SELECT * FROM users WHERE deleted_at IS NULL"
                cursor.execute(sql_statements)
                result = cursor.fetchall()
                cursor.close()
                users_return = []
                for value in result:
                    user = User(value[1], value[0], value[2], value[3], value[4])
                    users_return.append(user)
                return users_return
        except Exception as err:
            print("Get Users Error: ", err) 
    
    def create_user(self, user):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor()
                sql_statements = "INSERT INTO users (username) VALUES (%s) RETURNING *"
                data = [user.name]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                cursor.close()
                user_return = User(result[1], result[0], result[2], result[3], result[4])
                return user_return
        except Exception as err:
            print("Create User Error: ", err)
        return None

    def update_user(self, user):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor()
                sql_statements = "UPDATE users SET username = %s, updated_at = %s WHERE user_id = %s RETURNING *"
                data = [user.name, user.updated_at, user.id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                cursor.close()
                user_return = User(result[1], result[0], result[2], result[3], result[4])
                return user_return
        except Exception as err:
            print("Update User Error: ", err)
        return None

    def delete_user(self, user):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor()
                sql_statements = "UPDATE users SET deleted_at = %s WHERE user_id = %s RETURNING *"
                data = [user.deleted_at , user.id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                cursor.close()
                user_return = User(result[1], result[0], result[2], result[3], result[4])
                return user_return
        except Exception as err:
            print("Delete User Error: ", err)
        return None