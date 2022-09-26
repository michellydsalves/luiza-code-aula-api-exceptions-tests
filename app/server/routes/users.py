from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.models.response import ResponseModel, ErrorResponseModel
from app.server.models.users import UserSchema
from app.server.controller.users import UserController

router = APIRouter()
user_controller = UserController()

@router.post("/", response_description="Data do usuário de inclusão")
async def add_user(user: UserSchema = Body(...)):
    user_controller.add_user(user)
    user = jsonable_encoder(user)
    return ResponseModel(user, "Usuário incluido com sucesso")

@router.get("/", response_description="Lista de usuários")
async def list_users():
    users = user_controller.list_users()
    return jsonable_encoder(users)