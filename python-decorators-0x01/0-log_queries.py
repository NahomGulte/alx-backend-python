import sqlite3
import functools
from datetime import datetime
#### decorator to lof SQL queries

def log_sql_query(func):
    def wrapper(*args, **kwargs):
        query = args[1] if len(args) > 1 else "UNKNOWN QUERY"
        print(f" SQL LOG: Executing -> {query}")
        return func(*args, **kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
