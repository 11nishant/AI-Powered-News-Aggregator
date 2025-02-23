import os

class Config:
    DB_NAME = "news_aggregator"
    DB_USER = "vismay"  # Change if you set a different username
    DB_PASSWORD = "password"  # actual PostgreSQL password is "password" itself
    DB_HOST = "localhost"
    DB_PORT = "5432"  # Default PostgreSQL port

    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
