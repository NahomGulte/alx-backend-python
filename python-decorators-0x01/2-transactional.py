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

def transactional(func):
    def wrapper(*args, **kwargs):
        connection = None
            connection.begin()  
            result = func(connection, *args, **kwargs)  

            connection.commit()  
            print(" Transaction committed.")
            return result
        except Exception as e:
            if connection:
                connection.rollback()  
                print(" Transaction rolled back due to error:", e)
        finally:
            if connection and connection.open:
                connection.close()
                print("DB connection closed.")
    return wrapper
@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
cursor = conn.cursor() 
cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
