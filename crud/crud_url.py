from db.database import Database
from models.model_url import Url
from models.model_access_token import generate_access_token

class UrlCrud:
    
    def __init__(self):
        self.db = Database()
        
    def get_url(self, url_id):
        result = self.db.get_url(url_id)
        if not result:
            return "URL not exist in database"
        url_return = Url(result[1], result[6], result[0], result[2], result[3], result[4], result[5])
        if url_return.url_is_deleted():
            return "URL already deleted"
        return url_return
    
    def get_all_urls(self):
        result = self.db.get_urls()
        url_return = [Url(value[1], value[6], value[0], value[2], value[3], value[4], value[5]) for value in result]
        return url_return
        
    def create_url(self, orignal_url, creator_id):
        result = self.db.create_url(original_url=orignal_url, token_url=generate_access_token(), creator_id=creator_id)
        url_return = Url(result[1], result[6], result[0], result[2], result[3], result[4], result[5])
        return url_return
        
    def update_url(self, url_id, new_original_url = None):
        url_to_update = self.get_url(url_id)
        url_to_update.update_url(new_original_url)
        result = self.db.update_url(url_to_update.url_id, url_to_update.original_url, url_to_update.updated_at)
        url_return = Url(result[1], result[6], result[0], result[2], result[3], result[4], result[5])
        return url_return
    
    def delete_url(self, url_id):
        url_to_delete = self.get_url(url_id)
        if type(url_to_delete) is str:
            return url_to_delete
        url_to_delete.delete_url()
        result = self.db.delete_url(url_to_delete.url_id, url_to_delete.deleted_at)
        url_return = Url(result[1], result[6], result[0], result[2], result[3], result[4], result[5])
        return url_return