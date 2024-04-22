import pymysql.cursors
import os
from dotenv import load_dotenv 

load_dotenv() 

class Config:
    def __init__(self):
        self.db_conn = pymysql.connect(host=os.getenv("HOST"),
                             user=os.getenv("USER"),
                             password=os.getenv("PASSWORD"),
                             db='student_meal_express',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)