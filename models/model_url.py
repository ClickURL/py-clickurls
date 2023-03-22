from datetime import datetime
from config import settings

class Url:
    def __init__(self, **kwargs):
        self.id = kwargs["url_id"] if kwargs.get("url_id") else None
        self.original_url = kwargs["original_url"] if kwargs.get("original_url") else None
        self.short_url = kwargs["short_url"] if kwargs.get("short_url") else None
        self.secret_access_token = kwargs["secret_access_token"] if kwargs.get("secret_access_token") else None
        self.created_at = kwargs["created_at"] if kwargs.get("created_at") else None
        self.updated_at = kwargs["updated_at"] if kwargs.get("updated_at") else None
        self.deleted_at = kwargs["deleted_at"] if kwargs.get("deleted_at") else None
        self.creator_id = kwargs["creator_id"] if kwargs.get("creator_id") else None
        
        
        self.short_url_full = settings.localhost + ":" + str(settings.port) + "/" + self.short_url
        self.secret_access_token_full = settings.localhost + ":" + str(settings.port) + "/edit/" + str(self.secret_access_token)
        
    def update_url(self, new_original_url = None):
        if new_original_url:
            self.original_url = new_original_url
        self.updated_at = datetime.now()
        
    def delete_url(self):
        self.deleted_at = datetime.now()
        
    def url_is_deleted(self):
        if self.deleted_at:
            return True
        else:
            return False
