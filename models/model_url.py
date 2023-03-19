from datetime import datetime

class Url:
    def __init__(self, original_url, creator_id, url_id = None, token = None, created_at = None, updated_at = None, deleted_at = None):
        self.url_id = url_id
        self.original_url = original_url
        self.token = token
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
        self.creator_id = creator_id
        
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