from .base import ODBCBase
from .drivers import AzureSQLDriverVers, OracleDriverVersion

class AzureSQLConnector(ODBCBase):
    def __init__(self, server, database, user, password):
        super().__init__(
            driver=AzureSQLDriverVers.SQL_SERVER_2019,
            server=server,
            database=database,
            user=user,
            password=password
        )

    def azure_connect(self):
        self.connect()

    def azure_close(self):
        self.close()
        

class OracleConnector(ODBCBase):
    def __init__(self, server, database, user, password):
        super().__init__(
            driver=OracleDriverVersion.23c,
            server=server,
            database=database,
            user=user,
            password=password
        )

    def oracle_connect(self):
        self.connect()

    def oracle_close(self):
        self.close()

class PostgreSQLConnector(ODBCBase):
    def __init__(self, server, database, user, password):
        super().__init__(
            driver="{PostgreSQL Unicode}",
            server=server,
            database=database,
            user=user,
            password=password
        )

    def postgres_connect(self):
        self.connect()
    
    def postgres_close(self):
        self.close()

class MySQLConnector(ODBCBase):
    def __init__(self, server, database, user, password):
        super().__init__(
            driver="{MySQL ODBC 8.0 Unicode Driver}",
            server=server,
            database=database,
            user=user,
            password=password
        )

    def mysql_connect(self):
        self.connect()
    
    def mysql_close(self):
        self.close()

class SQLiteConnector(ODBCBase):
    def __init__(self, database):
        super().__init__(
            driver="{SQLite3 ODBC Driver}",
            server="",  # SQLite only needs a file-based database
            database=database
        )

    def sqlite_connect(self):
        self.connect()
    
    def sqlite_close(self):
        self.close()

class CosmosDBConnector(ODBCBase):
    def __init__(self, server, database, user, password):
        super().__init__(
            driver="{Cosmos DB ODBC Driver}",  # Example driver
            server=server,
            database=database,
            user=user,
            password=password
        )

    def cosmos_connect(self):
        self.connect()

    def cosmos_close(self):
        self.close()

