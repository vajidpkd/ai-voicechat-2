from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DEBUG: bool = True
    ALLOWED_ORIGINS: list[str] = ["http://localhost:19006"]

    class Config:
        env_file = ".env"

settings = Settings()
