import hashlib
from database_manager import DatabaseManager

db = DatabaseManager()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    if db.get_user(username):
        return False, "User already exists"
    db.add_user(username, hash_password(password))
    return True, "User registered successfully"

def authenticate(username, password):
    user = db.get_user(username)
    if not user:
        return False, "User not found"
    if hash_password(password) == user["password_hash"]:
        return True, "Login successful"
    else:
        return False, "Incorrect password"
