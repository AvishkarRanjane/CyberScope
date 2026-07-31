import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default-cyber-scope-key-2026")
    PHONE_API_KEY = os.getenv("PHONE_API_KEY", "")
    RATELIMIT_DEFAULT = "100 per day; 30 per hour"
    RATELIMIT_STORAGE_URI = "memory://"
