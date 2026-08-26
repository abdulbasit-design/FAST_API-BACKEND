from app.database.connection import users_collection


result = users_collection.update_many(
    {
        "role": {"$exists": False}
    },
    {
        "$set": {
            "role": "user"
        }
    }
)

print(f"Users updated: {result.modified_count}")