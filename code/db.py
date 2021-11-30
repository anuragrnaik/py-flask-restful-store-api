import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_connection():
    db_uri = os.getenv('DATABASE_URL', 'sqlite:///data.db')
    if db_uri and db_uri.startswith("postgres://"):
        db_uri = db_uri.replace("postgres://", "postgresql://", 1)
    return db_uri