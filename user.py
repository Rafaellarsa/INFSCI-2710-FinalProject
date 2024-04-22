import uuid

from config import Config

class User:
    def __init__(self, user_id="", username = "", email = ""):
        self.__username = username
        self.__email = email
        if user_id == "" and username != "":
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

    def set_username(self, username):
        self.__username = username
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE user SET username = %s WHERE user_id = %s;'
                print(qry)
                cur.execute(qry, (self.__username, self.__user_id)) 
                con.commit()
        finally:
            con.close()
    
    def set_email(self, email):
        self.__email = email
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE user SET email = %s WHERE user_id = %s;'
                print(qry)
                cur.execute(qry, (self.__email, self.__user_id)) 
                con.commit()
        finally:
            con.close()

    def get_by_id(self, user_id):
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = "SELECT * FROM users WHERE user_id = '" + user_id + "'"
                print(qry)
                cur.execute(qry)
                data = cur.fetchall()
                return data
        finally:
            con.close()