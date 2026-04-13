from fastapi import FastAPI 
from pydantic import BaseModel

class InputFeatures(BaseModel):
    input_: str

myapp = FastAPI()

@myapp.get("/")
def hello():
    return {"message":"Hello from batch1_2022BCS0050"}

@myapp.post("/input")
def predict(input_features: InputFeatures):
    return {"prediction": "Good", "rollno": "batch1_2022BCS0050"}