import pyodbc

class ODBCBase:
    def __init__(self, driver, server, database, user=None, password=None):
        self.driver = driver
        self.server = server
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        conn_str = (
            f"DRIVER={self.driver};"
            f"SERVER={self.server};"
            f"DATABASE={self.database};"
        )
        if self.user and self.password:
            conn_str += f"UID={self.user};PWD={self.password};"
        self.connection = pyodbc.connect(conn_str)

    def close(self):
        if self.connection:
            self.connection.close()