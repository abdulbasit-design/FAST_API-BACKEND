from fastapi import FastAPI

from app.routes.todo import router as todo_router
from app.routes.auth import router as auth_router

from app.middleware.middleware import log_requests

app = FastAPI()

app.middleware("http")(log_requests)


@app.get("/")
def hello():
    return {"message": "Welcome"}


app.include_router(todo_router)
app.include_router(auth_router)