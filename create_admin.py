from getpass import getpass

from app.database.connection import users_collection
from app.utils.password import hash_password


username = input("Enter admin username: ")
email = input("Enter admin email: ")
password = getpass("Enter admin password: ")


existing_user = users_collection.find_one({
    "$or": [
        {"email": email},
        {"username": username}
    ]
})


if existing_user:
    print("A user with this username or email already exists.")
else:

    hashed_password = hash_password(password)

    users_collection.insert_one({
        "username": username,
        "email": email,
        "password": hashed_password,
        "role": "admin"
    })

    print("Admin created successfully.")