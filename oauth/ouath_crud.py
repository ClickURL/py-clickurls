from db.database import Database
from oauth.user_social_profile import SocialProfile
from crud.crud_user import UserCrud
from oauth.provider_enum import Provider

class OAuthCrud():
    
    def __init__(self):
        self.db  = Database()
        
    def set_social_profile(self, user_info: dict):
        result_db = self.db.get_social_profiles_by_email(user_info["email"])  
        
        if not result_db:
            created_user_in_db = UserCrud().create_user()
            current_profile = SocialProfile(**user_info)
            current_profile.user_id = created_user_in_db.id
            profile_in_db = self.db.create_social_profile(current_profile)
        else:
            profile_by_provider = [profile for profile in result_db if profile["provider"] == Provider.google.value]
            current_profile = SocialProfile(**profile_by_provider[0])
            current_profile.update_social_provider()
            profile_in_db = self.db.update_social_profile(current_profile.id, current_profile.updated_at)
        
        current_profile = SocialProfile(**profile_in_db)
        return current_profile
    
    def get_social_profile(self, user_id):
        user_profile = self.db.get_social_profiles_by_user_id(user_id)
        return user_profile