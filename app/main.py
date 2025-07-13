from fastapi import FastAPI
from app.route import add_router

app = FastAPI()

add_router(app)
