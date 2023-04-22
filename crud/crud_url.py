from db.database import Database
from models.model_url import Url
from services.access_token import generate_access_token
from services.gen_short import generate_short_url
from services.url_validator import url_validator

class UrlCrud:
    
    def __init__(self):
        self.db = Database()
    
    def get_url_by_id(self, url_id):
        result = self.db.get_url_by_id(url_id)
        if not result:
            return "URL not exist in database"
        url_return = Url(**result)
        if url_return.url_is_deleted():
            return "URL already deleted"
        return url_return
    
    def get_url_by_token(self, token):
        result = self.db.get_url_by_token(token)
        if not result:
            return "URL not exist in database"
        url_return = Url(**result)
        if url_return.url_is_deleted():
            return "URL already deleted"
        return url_return
    
    def get_url_by_short(self, short):
        result = self.db.get_url_by_short(short)
        if not result:
            return "URL not exist in database"
        url_return = Url(**result)
        if url_return.url_is_deleted():
            return "URL already deleted"
        return url_return    
    
    def get_all_urls(self):
        result = self.db.get_urls()
        urls_return = [Url(**value) for value in result]
        return urls_return
    
    def get_urls_by_creator(self, creator_id):
        result = self.db.get_urls_by_user(creator_id)
        urls_return = [Url(**value) for value in result]
        return urls_return
        
    def create_url(self, orignal_url, creator_id):
        condition = True
        check_domain = url_validator(orignal_url)
        if not check_domain:
            raise Exception("Sorry, this domain is on the banned list")
        while condition:
            short_code = generate_short_url()
            if type(self.get_url_by_short(short_code)) is str:
                condition = False
        result = self.db.create_url(original_url=orignal_url, short_url=short_code, secret_access_token=generate_access_token(), creator_id=creator_id)
        url_return = Url(**result)
        return url_return
        
    def update_url(self, url_id, income_token, new_original_url = None):
        url_to_update = self.get_url_by_id(url_id)
        if type(url_to_update) is str:
            return url_to_update
        if income_token != str(url_to_update.secret_access_token):
            raise Exception("Sorry, Invalid secret token")
        url_to_update.update_url(new_original_url)
        result = self.db.update_url(url_to_update.id, url_to_update.original_url, url_to_update.updated_at, url_to_update.secret_access_token)
        url_return = Url(**result)
        return url_return
    
    def delete_url(self, url_id, income_token):
        url_to_delete = self.get_url_by_id(url_id)
        if type(url_to_delete) is str:
            return url_to_delete
        if income_token != str(url_to_delete.secret_access_token):
            raise Exception("Sorry, Invalid secret token")
        url_to_delete.delete_url()
        result = self.db.delete_url(url_to_delete.id, url_to_delete.deleted_at, url_to_delete.secret_access_token)
        url_return = Url(**result)
        return url_return
