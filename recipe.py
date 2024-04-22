import uuid

from config import Config

class Recipe:
    def __init__(self, recipe_id="", title = "", description = "", creation_date = "", cook_time = "", serving_size = "", created_by = ""):
        self.__recipe_id = recipe_id
        self.__title = title
        self.__description = description
        self.__creation_date = creation_date
        self.__cook_time = cook_time
        self.__serving_size = serving_size
        self.__created_by = created_by
    
    def get_all(self):
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = "SELECT * FROM recipes"
                cur.execute(qry)
                data = cur.fetchall()
                return data
        finally:
            con.close()

    def get_by_id(self, recipe_id):
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = "SELECT * FROM recipes"
                qry = qry + ' WHERE recipe_id = %s'
                cur.execute(qry, recipe_id)
                data = cur.fetchone()
                return data
        finally:
            con.close()

    def create(self):
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'INSERT INTO recipes (recipe_id, title, `description`, creation_date, cook_time, serving_size, created_by)'
                qry = qry + ' VALUES(%s, %s, %s, %s, %s, %s, %s)'
                cur.execute(qry, (self.__recipe_id, self.__title, self.__description, self.__creation_date, self.__cook_time, 
                                  self.__serving_size, self.__created_by)) 
                        
                con.commit()
                return self.get_by_id(self.__recipe_id)
        finally:
            con.close()

    def update(self):
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = "UPDATE recipes"
                qry = qry + ' SET title = %s, `description` = %s,  creation_date = %s, cook_time = %s, serving_size = %s, created_by = %s'
                qry = qry + ' WHERE recipe_id = %s'
                cur.execute(qry, (self.__title, self.__description, self.__creation_date, self.__cook_time, 
                                  self.__serving_size, self.__created_by, self.__recipe_id)) 
                con.commit()
                return self.get_by_id(self.__recipe_id)
        finally:
            con.close()

    def delete(self, recipe_id):
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = "DELETE FROM recipes"
                qry = qry + ' WHERE recipe_id = %s'
                cur.execute(qry, recipe_id)
                return {"message": ("Recipe with id " + recipe_id + " successfully deleted.")}
        finally:
            con.close()