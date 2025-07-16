import sqlite3

class SQLAdapter:
    def __init__(self, db_file='data.db'):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def run_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
