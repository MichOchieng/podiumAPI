import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict, prependCircuit, convertTime

app = FastAPI()

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
#     uvicorn.run(app, host="0.0.0.0", port=8000)