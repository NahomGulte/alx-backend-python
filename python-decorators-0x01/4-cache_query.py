import time
import pymysql
import functools


query_cache = {}
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

def cache_query(func):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if logger:
                logger(result)
            else:
                print(f"Query Result: {result}")
            return result
        return wrapper
    return decorator

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
