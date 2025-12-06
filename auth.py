from database_manager import DatabaseManager
import hashlib

db = DatabaseManager()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    if db.get_user(username):
        return False, "User already exists"

    password_hash = hash_password(password)
    db.add_user(username, password_hash)
    return True, "User registered successfully"


def authenticate(username, password):
    user = db.get_user(username)

    if not user:
        return False, "User not found"

    stored_hash = user[2]   

    if hash_password(password) == stored_hash:
        return True, "Login successful"
    else:
        return False, "Incorrect password"

