import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config:
    """Base application settings."""
    SECRET_KEY = os.getenv("SECRET_KEY", "medimate-ai-secret-key-default")
    DEBUG = os.getenv("FLASK_ENV", "development") == "development"
    PORT = int(os.getenv("PORT", 5000))
    
    BASE_DIR = BASE_DIR
    FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
    CONFIG_DIR = os.path.join(BASE_DIR, "config")
    
    FIREBASE_SERVICE_ACCOUNT = os.path.join(
        CONFIG_DIR, "firebase-service-account.json"
    )
    
    CORS_HEADERS = "Content-Type"
    JSON_SORT_KEYS = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
