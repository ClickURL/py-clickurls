from datetime import datetime

class User:
    def __init__(self, name, id = None, created_at = None, updated_at = None, deleted_at = None):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
        
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