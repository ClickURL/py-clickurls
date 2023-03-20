import schemas.schemas_url as url
import schemas.schemas_user as user
from pydantic import BaseModel

class UserUrlBase(user.UserGet):
    created_url: list[url.UrlBase]

