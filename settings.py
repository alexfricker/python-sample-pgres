import os

DB_SETTINGS = {
    "DB_NAME": os.environ.get("DB_NAME", "postgres"),
    "DB_USER": os.environ.get("DB_USER", "postgres"),
    "DB_PASSWORD": os.environ.get("DB_PASSWORD", "apples"),
    "DB_HOST": os.environ.get("DB_HOST", "localhost"),
    "DB_PORT": 5432,
}
