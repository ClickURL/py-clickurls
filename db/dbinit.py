import psycopg2 as db
from config import settings

INIT_STATEMENTS =  """CREATE TABLE IF NOT EXISTS PEOPLE (
        P_ID SERIAL PRIMARY KEY,
        NAME VARCHAR(100),
        EMAIL VARCHAR(120) UNIQUE
)"""


def initialize():
    with db.connect(settings.database_url) as connection:
        cursor = connection.cursor()
        cursor.execute(INIT_STATEMENTS)
        cursor.close()
