from fastapi import FastAPI
from typing import Optional
import math
from pydantic import BaseModel

class BhaskaraModel(BaseModel):
    a: int
    b: int
    c: int

class FraseModel(BaseModel):
    frase: str

app = FastAPI()

@app.get('/')
def index():
    return { 
        'data' : '/'
    }

@app.get('/quadrados')
def quadrados(max : Optional[int] = 10):
    quadrados = [];
    for i in range(0, max + 1, 1):
        quadrados.append(i ** 2);

    return {
        'data' : {
            'max' : max,
            'quadrados' : quadrados
        }
    }

@app.get('/tabuada/{num}')
def tabuada(num : int, start : Optional[int] = 1, end : Optional[int] = 10):
    tabuada = [];
    for i in range(start, end + 1, 1):
        tabuada.append(num * i);

    return {
        'data' : {
            'num' : num,
            'start' : start,
            'end' : end,
            'tabuada' : tabuada
        }
    }

@app.post('/bhaskara')
def bhaskara(termos : BhaskaraModel):
    x1 = (- termos.b + math.sqrt(- termos.b ** 2 - 4 * termos.a * termos.c)) / (2 * termos.a);
    x2 = (- termos.b - math.sqrt(- termos.b ** 2 - 4 * termos.a * termos.c)) / (2 * termos.a);
    return {
        'eq' : f'{termos.a}x^2 - {termos.b}x - {termos.c}',
        'x1' : x1,
        'x2' : x2
    }

@app.post('/conta')
def conta(frase : FraseModel):
    espacos = frase.frase.count(" ");
    vogais = 0;
    for x in frase.frase.lower():
        if x in ['a', 'e', 'i', 'o', 'u']:
            vogais += 1;
    outros = len(frase.frase) - (vogais + espacos); 
    return {
        'frase' : frase.frase,
        'vogais' : vogais,
        'espacos' : espacos,
        'outros' : outros
    }
