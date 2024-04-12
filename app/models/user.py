from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str

    def create_user(self):
        # Logic to create a new user
        pass

    def update_user(self):
        # Logic to update an existing user
        pass

    def delete_user(self):
        # Logic to delete a user
        pass

    @classmethod
    def get_user(cls, user_id: int):
        # Logic to get a user by ID
        pass

    @classmethod
    def get_all_users(cls):
        # Logic to get all users
        pass