from database_manager import DatabaseManager

db = DatabaseManager()

if db.cursor:
    db.cursor.execute("CREATE DATABASE IF NOT EXISTS cyber_platform")
    db.cursor.execute("USE cyber_platform")

    db.cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE,
        password_hash VARCHAR(255)
    )
    """)

    db.cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents (
        id INT AUTO_INCREMENT PRIMARY KEY,
        category VARCHAR(100),
        severity VARCHAR(50),
        status VARCHAR(50),
        description TEXT,
        incident_date DATE
    )
    """)

    db.conn.commit()
    print("Database initialized successfully")
