import pymysql

def stream_users_in_batches(batch_size):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="M0han_12",
        database="ALX_prodev",
        cursorclass=pymysql.cursors.DictCursor 
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM user_data")
            while True:
                rows = cursor.fetchmany(batch_size=1)
                if not rows:
                    break
                for row in rows:
                    yield row
    except pymysql.MySQLError as err:
        print("Fetch Error:", err)

def batch_processing():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM user_data WHERE age > 25")
            while True:
                rows = cursor.fetchmany(batch_size=10)
                if not rows:
                    break
                for row in rows:
                    return row
    except pymysql.MySQLError as err:
        print("Fetch Error:", err)
        
if __name__ == "__main__":

    try:
        user_generator = stream_users_in_batches(conn)  
        print("Generator type:", type(user_generator))  

        for user in user_generator:
            print("User:", user)

    finally:
        connection.close()
