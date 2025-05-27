import time
import pymysql 
import functools

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

def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except pymysql.MySQLError as e:
                    if e.args[0] in TRANSIENT_ERRORS:
                        attempts += 1
                        print(f"Transient error encountered (code {e.args[0]}): {e}")
                        print(f"Retrying... Attempt {attempts}/{max_retries}")
                        time.sleep(delay * attempts)  
                    else:
                        print("Non-transient DB error:", e)
                        break
            else:
                print("All retry attempts failed.")
        return wrapper
    return decorator
  


@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)
