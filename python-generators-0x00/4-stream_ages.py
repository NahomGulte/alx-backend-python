import pymysql

def connect_to_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="M0han_12",
        database="ALX_prodev",
        cursorclass=pymysql.cursors.DictCursor
    )

def stream_user_ages():
   
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT Age FROM user_data")
            for row in cursor:
                yield float(row['Age'])  
    finally:
        connection.close()

def calculate_average_age():
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1
    average = total / count if count > 0 else 0
    print(f"Average age of users: {average:.2f}")


if __name__ == "__main__":
    calculate_average_age()
