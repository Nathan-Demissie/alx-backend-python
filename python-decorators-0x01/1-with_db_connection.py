import sqlite3 
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')  # Open connection
        try:
            result = func(conn, *args, **kwargs)  # Pass connection to the function
        finally:
            conn.close()  # Ensure connection is closed
        return result
    return wrapper
