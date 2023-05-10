from datetime import datetime, timezone

class User:
    def __init__(self, **kwargs):
        self.id = kwargs["id"] if kwargs.get("id") else None
        self.name = kwargs["name"] if kwargs.get("name") else None
        self.created_at = kwargs["created_at"] if kwargs.get("created_at") else datetime.now(timezone.utc)
        self.updated_at = kwargs["updated_at"] if kwargs.get("updated_at") else None
        self.urls = []
        
    def update_user(self, new_name = None):
        if new_name:
            self.name = new_name
        self.updated_at = datetime.now(timezone.utc)
