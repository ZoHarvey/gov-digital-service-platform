# Sample FastAPI service

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'msg': 'Welcome to the Government Digital Platform API'}