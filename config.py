# config.py
# Sesuaikan DB credentials jika XAMPP MySQL punya password
import os
from dotenv import load_dotenv
load_dotenv()

DB_CONFIG = {
    "host": os.getenv('DB_HOST', 'localhost'),
    "user": os.getenv('DB_USER', 'root'),
    "password": os.getenv('DB_PASS', ''),
}

SECRET_KEY = os.getenv('SECRET_KEY', 'ganti_dengan_random_secret')
