import psycopg2

class DB:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(database="mapappdb", user="mapappdbuser", password="india!@1234", host="localhost", port="5432")
            print "database connected successfully"
        except:
            print "unable to connect to database"

        self.cursor = self.conn.cursor()
        #self.cursor = self.cnx.cursor(psycopg2.cursor.DictCursor)

    def execute(self, query, query_args=[]):
        self.cursor.execute(query, query_args)
        return self.cursor

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()
