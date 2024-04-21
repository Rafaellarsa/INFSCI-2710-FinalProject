import pymysql.cursors

import os
from dotenv import load_dotenv 
load_dotenv() 

db_connection = pymysql.connect(host=os.getenv("HOST"),
                             user=os.getenv("USER"),
                             password=os.getenv("PASSWORD"),
                             db='student_meal_express',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:

    with db_connection.cursor() as cur:

        cur.execute('SELECT * FROM recipes')

        rows = cur.fetchall()

        for row in rows:
            print(row)

finally:

    db_connection.close()