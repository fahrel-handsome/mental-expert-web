import mysql.connector
from config import DB_CONFIG

def connect_question():
    return mysql.connector.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        database="question_db"
    )
