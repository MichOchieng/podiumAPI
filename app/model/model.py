from cmath import log
import pickle
import datetime
import pandas as pd
from pathlib import Path

FILENAME = "treeModel.pkl"
BASE_DIR = Path(__file__).resolve(strict=True).parent

# Init model
with open(f"{BASE_DIR}/{FILENAME}", "rb") as file:
    model = pickle.load(file)

columns = [
    'avglap',
    'circuit_Albert Park Grand Prix Circuit',
    'circuit_Autodromo Enzo e Dino Ferrari',
    'circuit_Autodromo Internazionale del Mugello',
    'circuit_Autodromo Nazionale di Monza',
    'circuit_Autódromo Hermanos Rodríguez',
    'circuit_Autódromo Internacional do Algarve',
    'circuit_Autódromo José Carlos Pace',
    'circuit_Bahrain International Circuit', 'circuit_Baku City Circuit',
    'circuit_Circuit Gilles Villeneuve', 'circuit_Circuit Park Zandvoort',
    'circuit_Circuit Paul Ricard', 'circuit_Circuit de Barcelona-Catalunya',
    'circuit_Circuit de Monaco', 'circuit_Circuit de Spa-Francorchamps',
    'circuit_Circuit of the Americas', 'circuit_Hockenheimring',
    'circuit_Hungaroring', 'circuit_Istanbul Park',
    'circuit_Jeddah Corniche Circuit',
    'circuit_Losail International Circuit',
    'circuit_Marina Bay Street Circuit',
    'circuit_Miami International Autodrome', 'circuit_Nürburgring',
    'circuit_Red Bull Ring', 'circuit_Sepang International Circuit',
    'circuit_Shanghai International Circuit', 'circuit_Silverstone Circuit',
    'circuit_Sochi Autodrom', 'circuit_Suzuka Circuit',
    'circuit_Yas Marina Circuit'
]
# Init df
dataframe = pd.DataFrame(columns=columns).fillna(0.0)

# Convert Time to ms
def convertTime(time: str):
    minutes, seconds = time.split(":")
    seconds, milliseconds = seconds.split(".")
    delta = datetime.timedelta(minutes=float(minutes), seconds=float(
        seconds), milliseconds=float(milliseconds))

    ms = delta.total_seconds() * 1000.0
    return ms

# Prepend circuit_ to incoming circuit name
def prependCircuit(circuit: str):
    newName = 'circuit_' + circuit
    return newName


def predict(time: float, circuit: str):
    # Add vals to dataframe
    dataframe.at[0, 'avglap'] = time
    dataframe.at[0, circuit] = 1.0
    # Fill in NaN values
    dataframe.fillna(value=0.0, inplace=True)
    # Predict
    prediction = model.predict(dataframe)
    return prediction[0]
