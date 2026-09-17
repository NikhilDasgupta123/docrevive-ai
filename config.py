import os
from dotenv import load_dotenv
load_dotenv(override=True)

### Basic app.py info
APP_NAME = "DocRevive AI"
APP_VERSION = "1.0.0"

HOST = "127.0.0.1"
PORT = 8000

DEBUG = True

### Postgres DB details
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")