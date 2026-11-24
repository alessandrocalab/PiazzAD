import string
from app.core.constants import PASSWORD_MIN_LEN, PASSWORD_MAX_LEN

def validate_password(password: str)->str:
    if len(password) < PASSWORD_MIN_LEN or len(password) > PASSWORD_MAX_LEN
        raise ValueError(
            f"Password length must 
            be between {PASSWORD_MIN_LEN}
            and {PASSWORD_MAX_LEN} characters"
        )
    
    if not any(c.isupper() for c in password):
        raise ValueError("Password must contain an uppercase letter")

    if not any(c.islower() for c in password):
        raise ValueError("Password must contain an lowercase letter")

    if not any(c.isdigit() for c in password):
        raise ValueError("Password must contain a number")

    if not any(c in string.punctuation for c in password):
        raise ValueError("Password must contain a special character")
    
    return password