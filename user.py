import uuid

from config import Config

class User:
    def __init__(self, user_id="", username = "", email = "", password_hash = "", join_date = "", is_active = ""):
        self.__user_id = user_id
        self.__username = username
        self.__email = email
        self.__password_hash = password_hash
        self.__join_date = join_date
        self.__is_active = is_active

    def get_all(self):
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = "SELECT * FROM users"
                cur.execute(qry)
                data = cur.fetchall()
                return data
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

    def create(self):
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'INSERT INTO users (user_id, username, email, password_hash, join_date, is_active)'
                qry = qry + ' VALUES(%s, %s, %s, %s, %s, %s, %s)'
                cur.execute(qry, (self.__user_id, self.__username, self.__email, self.__password_hash, self.__join_date, self.__is_active)) 
                        
                con.commit()
                return self.get_by_id(self.__user_id)
        finally:
            con.close()

    def update(self):
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = "UPDATE users"
                qry = qry + ' SET username = %s, email = %s,  password_hash = %s, join_date = %s, is_active = %s'
                qry = qry + ' WHERE user_id = %s'
                cur.execute(qry, (self.__username, self.__email, self.__password_hash, self.__join_date, 
                                  self.__is_active)) 
                con.commit()
                return self.get_by_id(self.__user_id)
        finally:
            con.close()

    def delete(self, user_id):
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = "DELETE FROM users"
                qry = qry + ' WHERE user_id = %s'
                cur.execute(qry, user_id)
                return {"message": ("User with id " + user_id + " successfully deleted.")}
        finally:
            con.close()