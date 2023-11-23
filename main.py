#!/usr/bin/python3

from fastapi import FastAPI

app = FastAPI()

FAKE_DB = {
    1: {
        'Name': 'Bob',
        'Age': 32
    }
}

@app.get("/users/{userid}")
def get_user_by_id(uid: int):
    print(f'Received a request for user with ID: {uid}')
    if FAKE_DB.get(uid):
        return FAKE_DB.get(uid)
    else:
        return {'Error': 'User not found'}