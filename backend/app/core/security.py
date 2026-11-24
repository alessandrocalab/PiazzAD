from pwdlib import PasswordHash

password_hasher=PasswordHash.recommended()

def hash_password(password: str)->str:
    return password_hasher.hash(password)

def verify_password(password: str, hashed_password: str)->bool:
    return password_hasher.verify(password, hashed_password)


if __name__=="__main__":
    hash=hash_password("ciaomondo")
    print(hash)
    print(verify_password("ciaomondo", hash))