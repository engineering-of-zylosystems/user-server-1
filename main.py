from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from mangum import Mangum

# from zylo_docs.integration import add_zylo_docs

app = FastAPI()

class Pet(BaseModel):
    id: int
    name: str
    species: str
    age: Optional[int] = None
    
pets_db = [
    Pet(id=1, name="Fido", species="Dog", age=3),
    Pet(id=2, name="Whiskers", species="Cat", age=5),
    Pet(id=3, name="Rocky", species="Dog", age=1),
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Pet Store API"}

@app.get("/pets", response_model=List[Pet])
def get_pets():
    return pets_db

@app.get("/pets/{pet_id}", response_model=Pet)
def get_pet_by_id(pet_id: int):
    for pet in pets_db:
        if pet.id == pet_id:
            return pet
    return {"error": "Pet not found"}

@app.post("/pets", response_model=Pet)
def create_pet(pet: Pet):
    pets_db.append(pet)
    return pet

handler = Mangum(app)
# add_zylo_docs(app)