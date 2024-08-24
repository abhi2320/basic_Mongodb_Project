from fastapi import FastAPI, HTTPException, Body
from pymongo.collection import ReturnDocument
from models import User, hash_password, verify_password
from config import users_collection, linked_ids_collection
from bson import ObjectId
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class UserModel(BaseModel):
    username: str
    email: str
    password: str
    id: Optional[str]  # Optional field to handle ObjectId

    class Config:
        json_encoders = {
            ObjectId: str
        }

class LinkedIDModel(BaseModel):
    user_id: str
    linked_ids: List[str]
    
@app.post("/register/")
async def register_user(user: User):
    existing_user = users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user.password = hash_password(user.password)
    users_collection.insert_one(user.dict())
    return {"message": "User registered successfully"}

@app.post("/link-id/")
async def link_id(link_id_model: LinkedIDModel):
    email = link_id_model.email
    id_to_link = link_id_model.id_to_link

    print(f"Received email: {email}, ID to link: {id_to_link}")

    user = users_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    print(f"User found: {user}")

    result = linked_ids_collection.update_one(
        {"user_id": user["_id"]},
        {"$push": {"linked_ids": id_to_link}},
        upsert=True
    )

    print(f"Update result: {result}")

    return {"message": f"ID {id_to_link} linked to user {user['username']}"}

@app.get("/get-joined-data/")
async def get_joined_data(email: str):
    user = users_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    linked_ids = linked_ids_collection.find_one({"user_id": user["_id"]})
    if not linked_ids:
        raise HTTPException(status_code=404, detail="No linked IDs found for user")

    user_model = UserModel(username=user['username'], email=user['email'], password=user['password'], id=str(user['_id']))
    linked_id_model = LinkedIDModel(user_id=str(user["_id"]), linked_ids=linked_ids.get("linked_ids", []))

    return {"user": user_model.dict(), "linked_ids": linked_id_model.dict()}


@app.delete("/delete-user/")
async def delete_user(email: str):
    user = users_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    users_collection.delete_one({"_id": user["_id"]})
    linked_ids_collection.delete_one({"user_id": user["_id"]})
    return {"message": f"User {user['username']} and all related data deleted"}
