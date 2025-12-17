from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return{'message':'Website is Workingsssssssssssssaaaaaaaaaaaaaaaaaaassssss'}


@app.get('/Sai')
def set():
    return{'message':'Sai Sunil Varade'}


