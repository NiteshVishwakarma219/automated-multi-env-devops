import os

class Config:
    ENVIRONMENT = os.getenv("APP_ENV", "Development")