from db.database import Database
from models.model_user import User

class UserCrud:
    
    def __init__(self):
        self.db  = Database()
    
    def get_user(self, user_id):
        result = self.db.get_user(user_id)
        if not result:
            return "User not exist in database"
        user_return = User(**result)
        if user_return.user_is_deleted():
            return "User already deleted"
        return user_return
    
    def get_all_users(self):
        result = self.db.get_users()
        users_return = [User(**value) for value in result]
        return users_return
    
    def create_user(self, user_name):
        result = self.db.create_user(user_name)
        user_return = User(**result)
        return user_return
    
    def update_user(self, user_id, new_user_name = None):
        user_to_update = self.get_user(user_id)
        user_to_update.update_user(new_user_name)
        result = self.db.update_user(user_to_update.name, user_to_update.updated_at, user_to_update.id)
        user_return = User(**result)
        return user_return
    
    def delete_user(self, user_id):
        user_to_delete = self.get_user(user_id)
        if type(user_to_delete) is str:
            return user_to_delete
        user_to_delete.delete_user()
        result = self.db.delete_user(user_to_delete.id, user_to_delete.deleted_at)
        user_return = User(**result)
        return user_return
