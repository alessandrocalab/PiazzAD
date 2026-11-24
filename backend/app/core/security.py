import secrets
import hashlib
from pwdlib import PasswordHash

password_hasher=PasswordHash.recommended()

#generate a casual token with 32 random byte
def generate_session_token()->str:
    return secrets.token_urlsafe(32)

def hash_password(password: str)->str:
    return password_hasher.hash(password)

def verify_password(password: str, hashed_password: str)->bool:
    return password_hasher.verify(password, hashed_password)


#we use SHA-256 for session token
def hash_session_token(token: str)->str:
    return hashlib.sha256( #calcolate the hash
        token.encode("utf-8") #convert the str in byte
    ).hexdigest() #we need an hexadecimal format

if __name__=="__main__":
    hash=hash_password("ciaomondo")
    print(hash)
    print(verify_password("ciaomondo", hash))

    token=generate_session_token()
    print(token)
    print(hash_session_token(token))