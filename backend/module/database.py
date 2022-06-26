import pymysql


class Database:
    def connect(self):

        return pymysql.connect(host="localhost", user="root", password="123456", database="embargos", charset='utf8mb4')

    def read(self, query):
        con = Database.connect(self)
        cursor = con.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print('error ', e)
            return ()
        finally:
            con.close()

    def insert(self, query):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute(query)
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
