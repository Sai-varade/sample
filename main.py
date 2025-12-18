from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return{'message':'25'}


@app.get('/Sai')
def set():
    return{'message':'750'}


