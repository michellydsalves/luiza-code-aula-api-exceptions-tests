from pytest import fixture, raises, mark
from fastapi.exceptions import HTTPException

from app.server.controller.users import UserController
from app.server.models.users import UserSchema


@fixture
def user_controller():
    return UserController()

def test_valida_usuario_success(user_controller):
    user = UserSchema(
        name="Michelly Alves",
        age=18,
        cpf="0000000",
        email="michellydsalves@gmail.com"
    )
    
    result = user_controller.add_user(user)
    assert result == True


@mark.parametrize(
    "user",
    [
        UserSchema(
            name="Michelly Alves",
            age=17,
            cpf="0000000",
            email="michellydsalves@gmail.com"
        ),
        UserSchema(
            name="Paula Alves",
            age=101,
            cpf="0000000",
            email="michellydsalves@gmail.com"
        )
    ]
)
def test_valida_usuario_idade_error(user_controller, user):
    with raises(HTTPException) as err:
        user_controller.add_user(user)
    assert err.value.status_code == 400
    assert err.value.detail == "Usuário deve ser maior de 18 anos e menor de 100 anos."
