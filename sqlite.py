
import sqlite3
class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = ("""
        CREATE TABLE IF NOT EXISTS employess(
        id INTEGER PRIMARY KEY,
        Name text,
        job text,
        gender,
        age text,
        Email text,
        Mobail text,
        Address text
        )
""")
        self.con.execute(sql)
        self.con.commit()
    def insert(self,Name,job,gender,age,Email,Mobail,Address):
        self.cur.execute("INSERT INTO employess VALUES(NULL,?,?,?,?,?,?,?)",(Name,job,gender,age,Email,Mobail,Address))
        self.con.commit()

    def REMOVE(self,id):
            self.cur.execute("DELETE FROM employess WHERE id =?",(id, ))
            self.con.commit()

    def Update(self,id,Name,job,gender,age,Email,Mobail,Address):
                self.cur.execute("UPDATE employess SET Name=?,job=?,gender=?,age=?,Email=?,Mobail=?,Address=? WHERE id =?",(Name,job,gender,age,Email,Mobail,Address,id))
                self.con.commit()

    def fetch(self):
                self.cur.execute("SELECT * FROM employess")
                return self.cur.fetchall()
    