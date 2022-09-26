
from fastapi import HTTPException
from app.server.models.response import ErrorResponseModel
from app.server.models.users import UserSchema


users = []

class UserController():
    
    def users_validate(self, name):
        for user in users:
            if user.name == name:
                raise HTTPException(status_code=409, detail="Já existe um usuário com esse nome.")
    
    def add_user(self, user: UserSchema):
        if len(user.name) < 10:
            raise HTTPException(status_code=400, detail="Usuário deve conter mais de 10 caracteres.")
        
        if user.age < 18 or user.age > 100:
            raise HTTPException(status_code=400, detail="Usuário deve ser maior de 18 anos e menor de 100 anos.")
            
        self.users_validate(user.name)
        users.append(user)
        
        return True
    
    def list_users(self):
        return users