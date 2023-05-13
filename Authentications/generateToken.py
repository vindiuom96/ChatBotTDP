import jwt
import time

def generate_token_super( password , id):
    secret_key = "secret key"
    encoded_jwt = jwt.encode({"password": password,
                              "id":id,
                              "expire": int(time.time()) + 600
                              }, secret_key,
                             algorithm="HS256")
    return encoded_jwt

def validate_token(token , collection_name):
    try:
        decode = jwt.decode(token, "secretfgkkmkkrsdmgkkokhlvdnjfjfgkfkfkzdlfkglkjdigjodfskokddgomkjfgggkjfjmmngdkk",
                            algorithms=["HS256"])
        if decode['expire'] <= int(time.time()):
            return False
        admins = collection_name.aggregate([
            {
                "$search": {
                    "index": 'getUsername',
                    "compound": {
                        "should": [
                            {
                                "text": {
                                    "query": decode['username'],
                                    "path": "username"
                                }
                            },
                            {
                                "text": {
                                    "query": decode['password'],
                                    "path": "password"
                                }
                            }
                        ],
                        "minimumShouldMatch": 2
                    }
                }
            },
        ])
        admin_list = list(admins)
        if admin_list == []:
            return False
        return True
    except:
        return False