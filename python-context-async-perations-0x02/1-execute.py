import sqlite3

class ExecuteQuery:
    def __init__(self, query, params):
        self.query = query
        self.params = params
        self.conn = None
        self.result = None

    def __enter__(self):
        self.conn = sqlite3.connect('users.db')
        cursor = self.conn.cursor()
        cursor.execute(self.query, self.params)
        self.result = cursor.fetchall()
        return self.result

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()

# ✅ Use the context manager with the `with` statement
with ExecuteQuery("SELECT * FROM users WHERE age > ?", (25,)) as results:
    print(results)
