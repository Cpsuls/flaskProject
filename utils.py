import uuid

# import pysha3

def hasher(password: str) -> str:
    """Хеширование данных"""
    # return pysha3.sha3_224(password.encode("utf-8")).hexdigest()
    return password



def token_generator() -> str:
    """Генерация токена пользователя"""
    return str(uuid.uuid4()).replace("-", "")