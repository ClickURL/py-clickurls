from urllib.parse import urlparse

from db.database import Database

def url_validator(url: str):
    parts = urlparse(url)
    is_prohibited = Database().get_prohibited(parts.netloc)
    if not is_prohibited:
        return True
    return False