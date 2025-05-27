import pymysql

def connect_db():
    print("Trying to connect...")
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="M0han_12"
        )
        print("Connected to MySQL!")
        return connection
    except pymysql.MySQLError as err:
        print("Connection Error:", err)
        return None

def create_database(connection, db_name):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            print(f"Database '{db_name}' created successfully!")
    except pymysql.MySQLError as err:
        print("Database Creation Error:", err)

def connect_to_prodev(db_name):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="M0han_12",
            database="ALX_prodev" 
        )
        print(f"Connected to database '{db_name}'")
        return connection
    except pymysql.MySQLError as err:
        print("Connection to DB Error:", err)
        return None

def create_table(connection):
    table_sql = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        Age DECIMAL NOT NULL
    );
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(table_sql)
            print("Table 'users' created successfully!")
    except pymysql.MySQLError as err:
        print("Table Creation Error:", err)

def insert_data(connection, data):
    table_sql = """
    INSERT IGNORE INTO user_data  (user_id,name , email,age) VALUES ('1','Nahom Gulte Amene' ,'nahomamene@gmail.com','29');
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(table_sql)
            print("data is  inserted  successfully!")
    except pymysql.MySQLError as err:
        print("data  insertion  Error:", err)
def close_connection(connection):
    if connection and connection.open:
        connection.close()
        print("MySQL connection closed.")

# --- Main ---
if __name__ == "__main__":
    db_name = "ALX_prodev"

    # Step 1: Connect & create DB
    conn = connect_to_prodev(db_name)
    if conn:
        create_database(conn, db_name)
        insert_data(conn,db_name)
        close_connection(conn)
    # Step 2: Reconnect to that DB & create table
    db_conn = connect_to_prodev(db_name)
    if db_conn:
        create_table(db_conn)
        insert_data(db_conn,db_name)
        close_connection(conn)
