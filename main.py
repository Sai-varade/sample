from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return{'message':'Website is Workingsssssssssssssssssssssssssssssssssssssssss'}


@app.get('/Sai')
def set():
    return{'message':'Sai Sunil Varade'}


