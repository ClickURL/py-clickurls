from datetime import datetime
import psycopg2 as db
from psycopg2 import extras
from config import settings

extras.register_uuid()

class Database:
    
    def __init__(self):
        self.url = settings.database_url
    
    def get_user(self, user_id: int):
        try:
            with db.connect(self.url) as connection:
                cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                SELECT *
                FROM users
                WHERE id = %s
                """
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
            with db.connect(self.url) as connection:
                cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                SELECT *
                FROM users
                WHERE deleted_at IS NULL"""
                cursor.execute(sql_statements)
                result = cursor.fetchall()
                cursor.close()
                return result
        except Exception as err:
            print("Get Users Error: ", err)
            raise err

    def create_user(self, user_name):
        try:
            with db.connect(self.url) as connection:
                cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                INSERT INTO users (name, created_at)
                VALUES (%s, %s)
                RETURNING *
                """
                data = [user_name, datetime.now()]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                cursor.close()
                return result
        except Exception as err:
            print("Create User Error: ", err)
            raise err

    def update_user(self, user_name, user_updated_at, user_id):
        try:
            with db.connect(self.url) as connection:
                cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                UPDATE users
                SET username = %s,
                    updated_at = %s
                WHERE id = %s
                RETURNING *
                """
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
            with db.connect(self.url) as connection:
                cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                UPDATE users
                SET deleted_at = %s
                WHERE id = %s
                RETURNING *
                """
                data = [user_delete_at , user_id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                cursor.close()
                return result
        except Exception as err:
            print("Delete User Error: ", err)
            raise err
    
    
    def get_url_by_id(self, id):
        try:
            with db.connect(self.url) as connection:
                cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                SELECT *
                FROM urls
                WHERE id = %s
                """
                data = [id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                cursor.close()
                return result
        except Exception as err:
            print("Get URL DB Error: ", err)
            raise err
        
    def get_url_by_short(self, short_url):
        try:
            with db.connect(self.url) as connection:
                cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                SELECT *
                FROM urls
                WHERE short_url = %s
                """
                data = [short_url]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                cursor.close()
                return result
        except Exception as err:
            print("Get URL DB Error: ", err)
            raise err
    
    def get_url_by_token(self, secret_access_token):
        try:
            with db.connect(self.url) as connection:
                cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                SELECT *
                FROM urls
                WHERE secret_access_token = %s
                """
                data = [secret_access_token]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                cursor.close()
                return result
        except Exception as err:
            print("Get URL DB Error: ", err)
            raise err
            
    def get_urls(self):
        try:
            with db.connect(self.url) as connection:
                cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                SELECT *
                FROM urls
                WHERE deleted_at IS NULL"""
                cursor.execute(sql_statements)
                result = cursor.fetchall()
                cursor.close()
                return result
        except Exception as err:
            print("Get URLs DB Error: ", err)
            raise err
        
    def get_urls_by_user(self, user_id):
        try:
            with db.connect(self.url) as connection:
                cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                SELECT *
                FROM urls
                WHERE creator_id = %s
                    AND deleted_at IS NULL
                """
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
            with db.connect(self.url) as connection:
                cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                INSERT INTO urls (
                        original_url,
                        short_url,
                        secret_access_token,
                        created_at,
                        created_by
                    )
                VALUES (%s, %s, %s, %s, %s)
                RETURNING *
                """
                data = [original_url, short_url, secret_access_token, datetime.now(), creator_id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                return result
        except Exception as err:
            print("Create URL DB Error: ", err)
            raise err
            
    def update_url(self, url_id, new_original_url, updated_at, secret_access_token):
        try:
            with db.connect(self.url) as connection:
                cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                UPDATE urls
                SET original_url = %s,
                    updated_at = %s
                WHERE id = %s
                    AND secret_access_token = %s
                RETURNING *
                """
                data = [new_original_url, updated_at, url_id, secret_access_token]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                return result
        except Exception as err:
            print("Update URL DB Error: ", err)
            raise err
    
    def delete_url(self, url_id, deleted_at, secret_access_token):
        try:
            with db.connect(self.url) as connection:
                cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                UPDATE urls
                SET deleted_at = %s
                WHERE id = %s
                    AND secret_access_token = %s
                RETURNING *
                """
                data = [deleted_at, url_id, secret_access_token]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                return result
        except Exception as err:
            print("Delete URL DB Error: ", err)
            raise err
        
    def get_all_views(self):
        try:
            with db.connect(self.url) as connection:
                cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                SELECT *
                FROM hour_views
                """
                cursor.execute(sql_statements)
                result = cursor.fetchall()
                return result
        except Exception as err:
            print("Get Click DB Error: ", err)
            raise err
    
    def get_views_by_url(self, link_id):
        try:
            with db.connect(self.url) as connection:
                cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                SELECT *
                FROM hour_views
                WHERE link_id = %s
                """
                data = [link_id]
                cursor.execute(sql_statements, data)
                result = cursor.fetchall()
                return result
        except Exception as err:
            print("Get Click DB Error: ", err)
            raise err
    
    def get_views_group_by_time(self, secret_access_token):
        try:
            with db.connect(self.url) as connection:
                cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                SELECT day_series.days AS DAY,
                    COALESCE(stats.count, 0) AS count
                FROM (
                        SELECT date_trunc('day', dd)::date AS days
                        FROM generate_series (
                                (NOW() - INTERVAL '1 month' - INTERVAL '3 day')::timestamp,
                                (NOW() + INTERVAL '3 day')::timestamp,
                                '1 day'::INTERVAL
                            ) AS dd
                    ) AS day_series
                    LEFT JOIN (
                        SELECT DATE(DATE_TRUNC('days', hour_time)) AS DAY,
                            SUM(count) AS count
                        FROM public.hour_views
                        WHERE url_id = (
                                SELECT id
                                FROM urls
                                WHERE secret_access_token = %s
                            )
                            AND hour_time >= current_date - INTERVAL '1 month'
                        GROUP BY DAY
                        ORDER BY DAY
                    ) AS stats ON day_series.days = stats.day
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
            with db.connect(self.url) as connection:
                cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
                sql_statements = """
                INSERT INTO hour_views (url_id, hour_time)
                VALUES
                    (%s, DATE_TRUNC('hour', TIMESTAMP %s)) ON CONFLICT (url_id, hour_time) DO
                UPDATE
                SET
                    count = hour_views.count + 1
                RETURNING *;
                """
                data = [link_id, datetime.now()]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                return result
        except Exception as err:
            print("Create Click DB Error: ", err)
            raise err
    
    def get_prohibited(self, prohibited):
        try:
            with db.connect(self.url) as connection:
                cursor = connection.cursor()
                sql_statements = """
                SELECT name 
                FROM prohibited_domain 
                WHERE name = %s
                """
                data = [prohibited]
                cursor.execute(sql_statements, data)
                result = cursor.fetchone()
                return result
        except Exception as err:
            print("Prohibited check DB Error: ", err)
            raise err
