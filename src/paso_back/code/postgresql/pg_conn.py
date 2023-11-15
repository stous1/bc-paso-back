import psycopg2

class DBConnection:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Connected to database")
        except Exception as e:
            print(f"Unable to connect to database: {e}")

    def close(self):
        if self.conn is not None:
            self.conn.close()
            print("Database connection closed")
