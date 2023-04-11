import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.model.model import predict, prependCircuit, convertTime

app = FastAPI()
 
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://localhost",
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"]
)

class Inputs(BaseModel):
    time: str
    circuit: str

class Outputs(BaseModel):
    podium: bool

# Health check
@app.get('/')
def home():
    return {"Health": "Ok"}

@app.post("/predict",response_model=Outputs)
def _predict(payload: Inputs):
    # Convert time and fix circuit name
    time    = convertTime(payload.time)
    circuit = prependCircuit(payload.circuit)
    # Predict
    podium  = predict(time=time,circuit=circuit)
    return { "podium" : podium } 

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT",8000))
#     uvicorn.run(app, host="0.0.0.0", port=8000)