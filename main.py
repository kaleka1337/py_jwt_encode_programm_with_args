import sys
from functions import jwt_encode, jwt_encode_in_file, jwt_decode

if len(sys.argv) < 3:
    print("Usage: python main.py <command> <name> <password>")
elif sys.argv[1] == 'decode':
    if len(sys.argv) != 3:
        print("Usage: python main.py decode <token>")
    else:
        token_for_decode = sys.argv[2]
        print(jwt_decode(token_for_decode))
elif sys.argv[1] == 'encode+file':
    if len(sys.argv) != 4:
        print("Usage: python main.py encode+file <name> <password>")
    else:
        name = sys.argv[2]
        password = sys.argv[3]
        print(jwt_encode_in_file(name, password))
else:
    name = sys.argv[1]
    password = sys.argv[2]
    print(jwt_encode(name, password))