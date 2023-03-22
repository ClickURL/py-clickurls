from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str
    localhost: str
    port: int
    
    class Config:
        env_file=".env"
    
settings = Settings()