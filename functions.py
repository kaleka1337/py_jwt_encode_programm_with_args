import jwt
import datetime
from config import JWT_SECRET

def jwt_encode(name: str, passw: str) -> str:
    payload = {'name': name, 
               'password': passw, 
               'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
               'lte': str(datetime.datetime.utcnow())}
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')

def jwt_encode_in_file(name: str, passw: str) -> str:
    payload = {'name': name, 
               'password': passw, 
               'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
               'lte': str(datetime.datetime.utcnow())}
    encoded_jwt = jwt.encode(payload, JWT_SECRET, algorithm='HS256')
    with open('your_token.txt', 'w') as file:
        file.write(f'{encoded_jwt}\nWarning! When you create new token this token has been deleted.')
    return str(encoded_jwt)

def jwt_decode(token: str) -> str:
    return jwt.decode(token, JWT_SECRET, algorithms=['HS256'])