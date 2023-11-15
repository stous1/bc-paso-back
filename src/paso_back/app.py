from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

app = FastAPI()

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

auth_handler = AuthHandler()

# Clase para gestionar usuarios (en un entorno real, se usaría una base de datos)
class UserManager:
    def __init__(self):
        self.users = {"testuser": "testpassword"}

    def authenticate_user(self, username: str, password: str):
        if username in self.users and self.users[username] == password:
            return True
        return False

user_manager = UserManager()

# Dependencia para obtener el token y decodificarlo
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    return auth_handler.decode_jwt_token(token)

# Rutas
@app.post("/token")
def login(username: str, password: str):
    if user_manager.authenticate_user(username, password):
        token_data = {"sub": username}
        token = auth_handler.create_jwt_token(token_data)
        return {"access_token": token, "token_type": "bearer"}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

@app.get("/protected")
def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": "You are authenticated!", "user": current_user}




class app():
#     def __init__(self):
#         self.items = []
#         self.app = FastAPI()
        
#     def read_root():
#         return {"message": "¡Hola, FastAPI!"}

#     @app.get("/")
#     def read_root():
#         return {"message": "¡Hola, FastAPI!"}

#     @app.get("/items")
#     def read_items():
#         return {"items": items}

#     @app.post("/items")
#     def create_item(item: str):
#         items.append(item)
#         return {"item": item}

#     @app.put("/items/{item_id}")
#     def update_item(item_id: int, updated_item: str):
#         if 0 <= item_id < len(items):
#             items[item_id] = updated_item
#             return {"item_id": item_id, "item": updated_item}
#         return {"error": "Índice fuera de rango"}

#     @app.delete("/items/{item_id}")
#     def delete_item(item_id: int):
#         if 0 <= item_id < len(items):
#             deleted_item = items.pop(item_id)
#             return {"item_id": item_id, "deleted_item": deleted_item}
#         return {"error": "Índice fuera de rango"}