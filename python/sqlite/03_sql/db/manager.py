import sqlite3
class DBManager:

    def __init__(self,name_db=None):
        self.conn= sqlite3.connect(name_db)
        self.cursor = self.conn.cursor() 
    @ property
    def get_conn(self):
        diet={
            "conn":self.conn,
            "cursor":self.cursor
        }
        return diet 