from datetime import datetime

class User:
    def __init__(self, name: str, id: int | None = None, created_at: datetime | None = None, updated_at: datetime | None = None, deleted_at: datetime | None = None):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
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
