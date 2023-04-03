import psycopg2 as db
from psycopg2 import extras
from config import settings

extras.register_uuid()

class Database:
    
    def __init__(self):
        self.url = settings.database_url
    
    def get_user(self, user_id: int):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = "SELECT * FROM users WHERE user_id = %s"
                data = [user_id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                cursor.close()
                return result
        except Exception as err:
            print("Get User DB Error: ", err)
            raise err
    
    def get_users(self):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = "SELECT * FROM users WHERE deleted_at IS NULL"
                cursor.execute(sql_statements)
                result = cursor.fetchall()
                cursor.close()
                return result
        except Exception as err:
            print("Get Users Error: ", err)
            raise err

    def create_user(self, user_name):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = "INSERT INTO users (username) VALUES (%s) RETURNING *"
                data = [user_name]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                cursor.close()
                return result
        except Exception as err:
            print("Create User Error: ", err)
            raise err

    def update_user(self, user_name, user_updated_at, user_id):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = "UPDATE users SET username = %s, updated_at = %s WHERE user_id = %s RETURNING *"
                data = [user_name, user_updated_at, user_id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                cursor.close()
                return result
        except Exception as err:
            print("Update User Error: ", err)
            raise err

    def delete_user(self, user_id, user_delete_at):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = "UPDATE users SET deleted_at = %s WHERE user_id = %s RETURNING *"
                data = [user_delete_at , user_id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                cursor.close()
                return result
        except Exception as err:
            print("Delete User Error: ", err)
            raise err
    
    def get_url(self, column, value):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = "SELECT * FROM urls WHERE " + column + " = %s"
                data = [value]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                cursor.close()
                return result
        except Exception as err:
            print("Get URL DB Error: ", err)
            raise err
            
    def get_urls(self):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = "SELECT * FROM urls WHERE deleted_at IS NULL"
                cursor.execute(sql_statements)
                result = cursor.fetchall()
                cursor.close()
                return result
        except Exception as err:
            print("Get URLs DB Error: ", err)
            raise err
        
    def get_urls_by_user(self, user_id):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = "SELECT * FROM urls WHERE creator_id = %s AND deleted_at IS NULL"
                data = [user_id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchall()
                cursor.close()
                return result
        except Exception as err:
            print("Get User with URL DB Error: ", err)
            raise err
        
    def create_url(self, original_url, short_url, secret_access_token, creator_id):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = "INSERT INTO urls (original_url, short_url, secret_access_token, creator_id) VALUES (%s, %s, %s, %s) RETURNING *"
                data = [original_url, short_url, secret_access_token, creator_id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                return result
        except Exception as err:
            print("Create URL DB Error: ", err)
            raise err
            
    def update_url(self, url_id, new_original_url, updated_at):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = "UPDATE urls SET original_url = %s, updated_at = %s WHERE url_id = %s RETURNING *"
                data = [new_original_url, updated_at, url_id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                return result
        except Exception as err:
            print("Update URL DB Error: ", err)
            raise err
    
    def delete_url(self, url_id, deleted_at):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = "UPDATE urls SET deleted_at = %s WHERE url_id = %s RETURNING *"
                data = [deleted_at, url_id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                return result
        except Exception as err:
            print("Delete URL DB Error: ", err)
            raise err
        
    def get_all_views(self):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = "SELECT * FROM hour_views"
                cursor.execute(sql_statements)
                result = cursor.fetchall()
                return result
        except Exception as err:
            print("Get Click DB Error: ", err)
            raise err
    
    def get_views_by_url(self, link_id):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = "SELECT * FROM hour_views WHERE link_id = %s"
                data = [link_id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchall()
                return result
        except Exception as err:
            print("Get Click DB Error: ", err)
            raise err
    
    def get_views_group_by_time(self, secret_access_token):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                SELECT date(date_trunc('days', time)) AS day_views, COUNT(link_id) AS count_views FROM hour_views
                WHERE link_id = (SELECT url_id FROM urls
                    WHERE secret_access_token = %s
                ) and time >= current_date - interval '1 month'
                GROUP BY link_id, day_views
                ORDER BY day_views
                """
                data = [secret_access_token]
                cursor.execute(sql_statements, data)
                result = cursor.fetchall()
                return result
        except Exception as err:
            print("Get Click GROUP by time DB Error: ", err)
            raise err
    
    def create_view(self, link_id):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = "INSERT INTO hour_views (link_id) VALUES (%s) RETURNING *"
                data = [link_id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                return result
        except Exception as err:
            print("Create Click DB Error: ", err)
            raise err
    
    def get_prohibited(self, prohibited):
        try:
            with db.connect(self.url) as conection:
                cursor = conection.cursor()
                sql_statements = "SELECT domain FROM prohibited_domain WHERE domain = %s"
                data = [prohibited]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                return result
        except Exception as err:
            print("Prohibited check DB Error: ", err)
            raise err
