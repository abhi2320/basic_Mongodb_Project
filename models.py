from pydantic import BaseModel
from bson.objectid import ObjectId
import bcrypt

# User Registration Schema
class User(BaseModel):
    username: str
    email: str
    password: str

# Utility function to hash a password
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Utility function to verify a password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
