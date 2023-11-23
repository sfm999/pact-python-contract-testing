import requests

def get_user(uid: int):
    uri = 'http://localhost:8000/users/' + str(uid)
    return requests.get(uri).json()