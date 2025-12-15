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
                database=os.getenv("DB_NAME", "cybersecurity_platform")
            )
            self.cursor = self.conn.cursor(dictionary=True)
            print("Database connected")
        except mysql.connector.Error as e:
            print(f"Database connection failed: {e}")
            self.conn = None
            self.cursor = None

    def get_user(self, username):
        if self.cursor:
            self.cursor.execute(
                "SELECT * FROM users WHERE username=%s", (username,)
            )
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

    def add_incident(self, category, severity, status, description, incident_date):
        if self.cursor:
            self.cursor.execute(
                """
                INSERT INTO incidents
                (category, severity, status, description, incident_date)
                VALUES (%s,%s,%s,%s,%s)
                """,
                (category, severity, status, description, incident_date)
            )
            self.conn.commit()

    def incident_by_severity(self):
        self.cursor.execute("""
            SELECT severity, COUNT(*) count
            FROM incidents
            GROUP BY severity
        """)
        return self.cursor.fetchall()

    def incident_by_category(self):
        self.cursor.execute("""
            SELECT category, COUNT(*) count
            FROM incidents
            GROUP BY category
        """)
        return self.cursor.fetchall()

    def incident_status_trend(self):
        self.cursor.execute("""
            SELECT incident_date, COUNT(*) count
            FROM incidents
            GROUP BY incident_date
            ORDER BY incident_date
        """)
        return self.cursor.fetchall()
