from datetime import datetime, timezone
from oauth.provider_enum import Provider

class SocialProfile():
    def __init__(self, **kwargs):
        self.id = kwargs["id"] if kwargs.get("id") else None
        self.user_id = kwargs["user_id"] if kwargs.get('user_id') else None
        self.provider = kwargs["provider"] if kwargs.get("provider") else Provider.google.value
        self.social_id = kwargs["id"] if kwargs.get("id") else None
        self.email = kwargs["email"] if kwargs.get("email") else None
        self.username = kwargs["name"] if kwargs.get("name") else None
        self.created_at = kwargs["created_at"] if kwargs.get("created_at") else datetime.now(timezone.utc)
        self.updated_at = kwargs["updated_at"] if kwargs.get("updated_at") else datetime.now(timezone.utc)
        
    def update_social_provider(self):
        self.updated_at = datetime.now(timezone.utc)
        
    def return_list_db(self):
        result_list = [self.user_id, self.provider, self.social_id, self.email, self.username, self.created_at, self.updated_at]
        return result_list
    
    def set_user_info_dict(self, user_info: dict):
        self.social_id = user_info["id"] if user_info.get("id") else None
        self.email = user_info["email"] if user_info.get("email") else None
        self.username = user_info["name"] if user_info.get("name") else None