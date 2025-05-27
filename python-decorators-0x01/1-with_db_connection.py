import sqlite3 
import functools
import pymysql
def with_db_connection(func):
      def wrapper(*args, **kwargs):
        connection = None
        try:
            print("Opening DB connection...")
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="M0han_12",
                database="ALX_prodev"
            )
            result = func(connection, *args, **kwargs)
            return result
        except pymysql.MySQLError as e:
            print("DB Error:", e)
        finally:
            if connection and connection.open:
                connection.close()
                print("DB connection closed.")
    return wrapper

@with_db_connection 
def get_user_by_id(conn, user_id): 
cursor = conn.cursor() 
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
return cursor.fetchone() 
#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id=1)
print(user)
