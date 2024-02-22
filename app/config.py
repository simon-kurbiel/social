from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    SECRET_KEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    SQLALCHEMY_DATABASE_URL:str
    
    class Config:
        env_file='.env'
    
settings = Settings()