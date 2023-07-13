from fastapi import FastAPI, HTTPException
from enum import Enum
from pydantic import BaseModel
from typing import Optional


app = FastAPI()
data = []

class FirstName(str,Enum):
    galih = "Galih"
    galer = "Galer"
    Abeh = "Abeh"

@app.get('/')
async def home():
    return "Ini Home"

@app.get('/home/{first_name}')
async def Users(first_name:FirstName):
    if first_name == FirstName.galih:
        return {"Nama saya":first_name}
    if first_name.value == "Galer":
        return{"Nama saya":first_name}
    return {"Nama saya":first_name}

class Items(BaseModel):
    name : str
    handphone : str
    alamat : str
    hobi : Optional[str]


@app.post('/users')
async def create_users(users:Items):
    inputan_data = users
    data.append(inputan_data)
    return data

@app.delete('/users/{index}')
async def delete_user(index: int):
    try:
        deleted_user = data.pop(index)
        return {"message": f"User at index {index} has been deleted", "user": deleted_user}
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")