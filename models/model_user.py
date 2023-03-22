from datetime import datetime

class User:
    def __init__(self, **kwargs):
        self.id = kwargs["user_id"] if kwargs.get("user_id") else None
        self.name = kwargs["user_name"] if kwargs.get("user_name") else None
        self.created_at = kwargs["created_at"] if kwargs.get("created_at") else None
        self.updated_at = kwargs["updated_at"] if kwargs.get("updated_at") else None
        self.deleted_at = kwargs["deleted_at"] if kwargs.get("deleted_at") else None
        self.urls = []
        
    def update_user(self, new_name = None):
        if new_name:
            self.name = new_name
        self.updated_at = datetime.now()
        
    def delete_user(self):
        self.deleted_at = datetime.now()
    
    def user_is_deleted(self):
        if self.deleted_at:
            return True
        else:
            return False
