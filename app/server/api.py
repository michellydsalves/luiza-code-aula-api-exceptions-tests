from fastapi import FastAPI
from app.server.routes.users import router as UserRouter


app = FastAPI()

app.include_router(UserRouter, tags="User", prefix="/users")

@app.get("/", tags="Root")
async def read_root():
    return {"message": "Bem-vindo a app"}