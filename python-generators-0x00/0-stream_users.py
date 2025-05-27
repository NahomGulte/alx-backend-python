import pymysql

def stream_users():
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="M0han_12",
            database="ALX_prodev",
        )
    
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM user_data ")
            while True:
                rows= cursor.fetchmany()
                if not rows:
                    break
                for row in rows:
                    yield row
                    
    except pymysql.MySQLError as err:
        print("Fetching error with" ,err)

    finally:
        if 'connection' in locals() and connection.open:
            connection.close()
            print("MySQL connection closed.")
            
if __name__ == "__main__":
    for user in stream_users():
        print("👤", user)
