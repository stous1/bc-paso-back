from jose import JWTError, jwt
from fastapi import HTTPException, status

# Configuración
SECRET_KEY = "bacf0427070825830b8e2dc64088c8793c86cf4a0b8993f22ecc0531b71c9bd0"
ALGORITHM = "HS256"

# Clase para gestionar la autenticación
class AuthHandler:
    @staticmethod
    def create_jwt_token(data: dict):
        return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def decode_jwt_token(token: str):
        try:
            return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )