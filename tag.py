from config import Config

class Tag:
    def __init__(self, tag_id="", name = "", description = ""):
        self.__tag_id = tag_id
        self.__name = name
        self.__description = description

    def get_all(self):
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = "SELECT * FROM tags"
                cur.execute(qry)
                data = cur.fetchall()
                return data
        finally:
            con.close()

    def get_by_id(self, tag_id):
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = "SELECT * FROM tags"
                qry = qry + ' WHERE tag_id = %s'
                cur.execute(qry, tag_id)
                data = cur.fetchone()
                return data
        finally:
            con.close()

    def create(self):
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'INSERT INTO tags (tag_id, `name`, `description`)'
                qry = qry + ' VALUES(%s, %s, %s)'
                cur.execute(qry, (self.__tag_id, self.__name, self.__description)) 
                con.commit()
                return self.get_by_id(self.__tag_id)
        finally:
            con.close()

    def update(self):
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = "UPDATE tags"
                qry = qry + ' SET `name` = %s, `description` = %s  WHERE tag_id = %s'
                cur.execute(qry, (self.__name, self.__description, self.__tag_id)) 
                con.commit()
                return self.get_by_id(self.__tag_id)
        finally:
            con.close()

    def delete(self, tag_id):
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = "DELETE FROM tags"
                qry = qry + ' WHERE tag_id = %s'
                cur.execute(qry, tag_id)
                return {"message": ("Tag with id " + tag_id + " successfully deleted.")}
        finally:
            con.close()