import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_NAME = os.getenv(
    "DATABASE_NAME",
    "spira_x.db"
)

ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    "development"
)

DEBUG = os.getenv(
    "DEBUG",
    "false"
).lower() == "true"