import uuid

from config import Config

class Recipe:
    def __init__(self, user_id="", username = "", email = ""):
        self.__user_id = user_id
        self.__username = username
        self.__email = email
        if user_id == "" and username != "":
            self.__user_id = str(uuid.uuid4())
            try: 
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO users (user_id, username, email)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__user_id, self.__username, self.__email)) 
                    con.commit()
            finally:
                con.close()

    def get_username(self):
        return self.__username
    
    def get_email(self):
        return self.__email
    
    def get_user_id(self):
        return self.__user_id
    
    def get_all(self):
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = "SELECT * FROM recipes"
                print(qry)
                cur.execute(qry)
                data = cur.fetchall()
                return data
        finally:
            con.close()