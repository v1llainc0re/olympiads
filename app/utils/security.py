from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

def hash_password(password: str) -> str:
    if not isinstance(password, str):
        raise TypeError("Пароль должен быть строкой")
    return ph.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        ph.verify(hashed_password, plain_password)
        return True
    except VerifyMismatchError:
        return False
    except Exception:
        return False

def needs_rehash(hashed_password: str) -> bool:
    try:
        return ph.check_needs_rehash(hashed_password)
    except Exception:
        return True