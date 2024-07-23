import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

class Config:
    IS_PRODUCTION = os.environ.get("FLASK_ENV") == "production"
    VITE_ORIGIN = os.environ.get("VITE_ORIGIN")

    APPLICATION_ROOT = os.path.dirname(os.path.abspath(__file__))

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")