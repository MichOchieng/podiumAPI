import pickle
import datetime
import pandas as pd
from pathlib import Path

FILENAME = ""
BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/{FILENAME}","rb") as file:
    model = pickle.load(file)

columns = [
    'avglap',
    'circuit_Albert Park Grand Prix Circuit',
    'circuit_Autódromo José Carlos Pace',
    'circuit_Autodromo Nazionale di Monza',
    'circuit_Autódromo Hermanos Rodríguez',
    'circuit_Autódromo Internacional do Algarve',
    'circuit_Autódromo José Carlos Pace',
    'circuit_Bahrain International Circuit',
    'circuit_Baku City Circuit',
    'circuit_Circuit de Barcelona-Catalunya',
    'circuit_Circuit de Monaco',
    'circuit_Circuit de Spa-Francorchamps',
    'circuit_Circuit Gilles Villeneuve',
    'circuit_Circuit of the Americas',
    'circuit_Circuit Park Zandvoort',
    'circuit_Circuit Paul Ricard',
    'circuit_Hockenheimring',
    'circuit_Hungaroring',
    'circuit_Istanbul Park',
    'circuit_Jeddah Corniche Circuit',
    'circuit_Losail International Circuit',
    'circuit_Marina Bay Street Circuit',
    'circuit_Miami International Autodrome',
    'circuit_Nürburgring',
    'circuit_Red Bull Ring',
    'circuit_Sepang International Circuit',
    'circuit_Shanghai International Circuit',
    'circuit_Silverstone Circuit',
    'circuit_Sochi Autodrom',
    'circuit_Suzuka Circuit',
    'circuit_Yas Marina Circuit',
]

dataframe = pd.DataFrame(0.0, columns=columns)

# Convert Time to ms
def convertTime(time:str):
    minutes, seconds = time.split(":")
    seconds, milliseconds = seconds.split(".")
    delta =  datetime.timedelta(minutes=float(minutes),seconds=float(seconds),milliseconds=float(milliseconds))

    ms = delta.total_seconds() * 1000.0
    return ms

# Prepend circuit_ to incoming circuit name
def prependCircuit(circuit:str):
    return 'circuit_' + circuit

def predict(time: float, circuit: str):
    # Add vals to dataframe
    dataframe['avglap'] = time
    dataframe[circuit] = 1.0
    # Format for prediction - could probably do this from the start
    return model.predict(pd.DataFrame([dataframe.values],columns=columns))