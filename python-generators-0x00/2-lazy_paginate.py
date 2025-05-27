import pymysql

def connect_to_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="M0han_12",
        database="ALX_prodev",
        cursorclass=pymysql.cursors.DictCursor
    )

def paginate_users(connection, page_size, offset):
    """Fetch a page of users from the database."""
    with connection.cursor() as cursor:
        query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        return cursor.fetchall()

def lazy_paginate(page_size):
    """Generator function to yield pages of users lazily."""
    connection = connect_to_db()
    offset = 0

    try:
        while True:
            users = paginate_users(connection, page_size, offset)
            if not users:
                break
            yield users
            offset += page_size
    finally:
        connection.close()

# --- Usage Example ---
if __name__ == "__main__":
    for page in lazy_paginate(2):  # Replace 2 with your desired page size
        print("Page:")
        for user in page:
            print(user)
