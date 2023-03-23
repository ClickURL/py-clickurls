from db.database import Database
from models.model_views import View

class ViewCrud:
    
    def __init__(self):
        self.db = Database()
        
    def get_all_views(self):
        result = self.db.get_all_views()
        views_return = [View(**value) for value in result]
        return views_return
    
    def get_stats_group_by_time(self, secret_access_token):
        result = self.db.get_views_group_by_time(secret_access_token)
        return result
    
    def create_view(self, link_id):
        result = self.db.create_view(link_id)
        view_return = View(**result)
        return view_return