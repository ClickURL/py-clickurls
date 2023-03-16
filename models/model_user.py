from datetime import datetime

class User:
    def __init__(self, name, id = None, created_at = None, updated_at = None, deleted_at = None):
        self.name = name
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
        
    def update_user(self, new_name):
        self.name = new_name
        self.updated_at = datetime.now()
        
    def delete_user(self):
        self.deleted_at = datetime.now()