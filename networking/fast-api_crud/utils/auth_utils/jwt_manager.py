import bcrypt
import jwt
import json

from utils.config_reader import read_config

# info = read_config("data/config.txt")
# SECRET_KEY=(info["jwt_secret"])
from utils.json_file_utils import load_json

SECRET_KEY="d640ef9b7d9a43aa415dc6242585899a"
def generate_jwt(payload):
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    print('encoded_jwt: ', encoded_jwt)
    return encoded_jwt


def verify_jwt(user_jwt,username:str,file_path):
    try:
        db_tokens=load_json(file_path)

        if username in db_tokens:
            if db_tokens[username]==user_jwt:
                data = jwt.decode(user_jwt, SECRET_KEY, algorithms="HS256")
                result=data["user role"]
                # print("data",data["user role"])
                # print("data",data["username"])
                print(result)
                return result  # Token is valid
            else:
                return False
    except jwt.ExpiredSignatureError:
        print("Token has expired")
        return False  # Token is expired
    except jwt.InvalidTokenError:
        print("Invalid token")
        return False  # Token is invalid


def check_token(request,username:str,file_path):
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        try:
            result=verify_jwt(token,username,file_path)
            return result
        except Exception as e:
            raise e
    return
# verify_jwt("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjEiLCJ1c2VyIHJvbGUiOiJhZG1pbiJ9.ej4MIs3H05mGVMdKK-vOmN4v-o2ZFhoQYFgGMrflwI4")
# def jwt_test():
#     # Define the secret key
#     SECRET_KEY = "your-secret-key"

#     # Generate a JWT token
#     payload = {"user_id": 123}
#     token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

#     # Verify the JWT token
#     try:
#         decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#         print("Decoded Payload:", decoded_payload)
#     except jwt.ExpiredSignatureError:
#         print("Token has expired")
#     except jwt.InvalidTokenError:
#         print("Invalid token")
# jwt_test()
