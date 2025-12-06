import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class DatabaseManager:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host=os.getenv("DB_HOST", "localhost"),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", ""),
                database=os.getenv("DB_NAME", "cyber_platform")
            )
            self.cursor = self.conn.cursor(dictionary=True)
            print("Database connected")
        except mysql.connector.Error as e:
            print(f" Database connection failed: {e}")
            self.conn = None
            self.cursor = None

    def get_user(self, username):
        if self.cursor:
            self.cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
            return self.cursor.fetchone()
        return None

    def add_user(self, username, password_hash):
        if self.cursor:
            self.cursor.execute(
                "INSERT INTO users (username, password_hash) VALUES (%s,%s)",
                (username, password_hash)
            )
            self.conn.commit()

    def fetch_incidents(self):
        if self.cursor:
            self.cursor.execute("SELECT * FROM incidents")
            return self.cursor.fetchall()
        return []
