from fastapi import FastAPI
from pydantic import BaseModel #data form checker

app = FastAPI()

user_db = {
    1: {"name": "Sulaxmi", "age": 27},
    2: {"name": "Sakshi", "age": 21},
    3: {"name": "Test", "age": 37},
}

class User(BaseModel):
    name: str
    age: int

#app - fast api variable to expose api
# @app.get("/users")
# def print_users():
#     return user_db


@app.put("/users/v1/update/{user_id}")
def user_update(user_id: int, user_details: User):
    if user_id in user_db:
        user_db[user_id] = user_details.dict()
        return {"message": "User updated", "User": user_db[user_id]}
    else:
        return {"message": "Sorry, not found!"}
    

@app.delete("/users/v1/delete/{user_id}")
def delete_user(user_id: int):
    if user_id in user_db:
        del user_db[user_id]
        return {"message": "User deleted"}
    else:
        return {"message": "Sorry, not found!"}



