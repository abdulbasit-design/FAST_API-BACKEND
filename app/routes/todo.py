from fastapi import APIRouter, Depends, HTTPException
from app.schemas.todo import Todo
from app.database.connection import todos_collection
from app.utils.auth import get_current_user, require_admin

router = APIRouter()


@router.get("/admin-test")
def admin_test(
    current_user: dict = Depends(require_admin)
):
    return {
        "message": "Welcome Admin",
        "user": current_user
    }


@router.post("/todos")
def create_todo(
    todo: Todo,
    current_user=Depends(get_current_user)
):

    todo_data = todo.model_dump()

    todo_data["owner_id"] = current_user["user_id"]

    todos_collection.insert_one(todo_data)

    return {"message": "Todo is Added"}


@router.get("/todos")
def get_todos(
    current_user=Depends(get_current_user)
):

    if current_user["role"] == "admin":
        todos = todos_collection.find(
            {},
            {"_id": 0}
        )

    else:
        todos = todos_collection.find(
            {
                "owner_id": current_user["user_id"]
            },
            {"_id": 0}
        )

    return list(todos)


@router.get("/todos/{todo_id}")
def get_todo(
    todo_id: int,
    current_user=Depends(get_current_user)
):

    todo = todos_collection.find_one(
        {"id": todo_id},
        {"_id": 0}
    )

    if not todo:
        return {"error": "Todo not found"}

    if current_user["role"] == "admin":
        return todo

    if todo["owner_id"] != current_user["user_id"]:
        raise HTTPException(
            status_code=403,
            detail="You are not allowed to access this Todo"
        )

    return todo


@router.put("/todos/{todo_id}")
def update_todo(
    todo_id: int,
    updated_todo: Todo,
    current_user=Depends(get_current_user)
):

    todo = todos_collection.find_one({
        "id": todo_id
    })

    if not todo:
        return {"error": "Todo not found"}

    if current_user["role"] != "admin":

        if todo["owner_id"] != current_user["user_id"]:
            raise HTTPException(
                status_code=403,
                detail="You are not allowed to update this Todo"
            )

    todo_data = updated_todo.model_dump()

    result = todos_collection.update_one(
        {"id": todo_id},
        {"$set": todo_data}
    )

    return {"message": "Todo Updated"}


@router.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: int,
    current_user=Depends(get_current_user)
):

    todo = todos_collection.find_one({
        "id": todo_id
    })

    if not todo:
        return {"error": "Todo not found"}

    if current_user["role"] != "admin":

        if todo["owner_id"] != current_user["user_id"]:
            raise HTTPException(
                status_code=403,
                detail="You are not allowed to delete this Todo"
            )

    result = todos_collection.delete_one({
        "id": todo_id
    })

    return {"message": "Todo Deleted"}