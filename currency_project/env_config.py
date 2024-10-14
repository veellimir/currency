import os

from dotenv import load_dotenv

load_dotenv()

CONFIG__SECRET_KEY = os.getenv("SECRET_KEY")
CONFIG__PROJECT_DOMAIN_NAME = os.getenv("PROJECT_DOMAIN_NAME")
CONFIG__DEBUG = os.getenv("DEBUG")

CONFIG__API_CURRENCY = os.getenv("API_CURRENCY")