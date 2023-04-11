# Podium API

Simple FastAPI for decision tree model that predicts whether a driver in a Formula 1 race will finish in the top 3 (podium) a specific circuit given an average lap time.

## Endpoints

@app.get('/')
- Returns API healthcheck with status "Ok"

@app.post("/predict")

Inputs 
```python
class Inputs(BaseModel):
    time: str
    circuit: str
```

Outputs
```python
class Outputs(BaseModel):
    podium: bool
```
## Examples

JSON Request Body for /predict endpoint
```JSON
{
    time: "1:20.235",
    circuit: "Albert Park Grand Prix Circuit"
}
```

JSON Response
```JSON
{
    podium: true
}
```
