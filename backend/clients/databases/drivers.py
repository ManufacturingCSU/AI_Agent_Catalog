from enum import Enum

class AzureSQLDriverVersion(str, Enum):
    SQL_SERVER_2022 = "{ODBC Driver 18 for SQL Server}"
    SQL_SERVER_2019 = "{ODBC Driver 17 for SQL Server}"
    SQL_SERVER_2017 = "{ODBC Driver 13 for SQL Server}"
    SQL_SERVER_2016 = "{SQL Server}"
    SQL_SERVER_2014 = "{SQL Server Native Client 11.0}"
    SQL_SERVER_2012 = "{SQL Server Native Client 11.0}"

class OracleDriverVersion(str, Enum):
    "23c" = "{Oracle ODBC Driver 23c}",
    "21c" = "{Oracle ODBC Driver 21c}",
    "19c" = "{Oracle ODBC Driver 19c}",
    "18c" = "{Oracle ODBC Driver 18c}",
    "12c" = "{Oracle ODBC Driver 12c Release 2 (12.2)}"

class PostgreSQLDriverVersion(str, Enum):
    "16" = "{PostgreSQL ODBC Driver 16}",
    "15" = "{PostgreSQL ODBC Driver 15}",
    "14" = "{PostgreSQL ODBC Driver 14}",
    "13" = "{PostgreSQL ODBC Driver 13}",
    "12" = "{PostgreSQL ODBC Driver 12}",

class MySQLDriverVersion(str, Enum):
    "8.0" = "{MySQL ODBC 8.0 Driver}",
    "5.7" = "{MySQL ODBC 5.3 ANSI Driver}",
    "5.6" = "{MySQL ODBC 5.2 ANSI Driver}",
    "5.5" = "{MySQL ODBC 5.1 ANSI Driver}",
    "5.1" = "{MySQL ODBC 5.1 ANSI Drive = }",

class SQLiteDriverVersion(str, Enum):
    "3.48.0" = "{SQLite ODBC Driver 3.48.0}",
    "3.47.2" = "{SQLite ODBC Driver 3.47.2}",
    "3.47.1" = "{SQLite ODBC Driver 3.47.1}",
    "3.47.0" = "{SQLite ODBC Driver 3.47.0}",
    "3.46.0" = "{SQLite ODBC Driver 3.46.0}",

class CosmosDBDriverVersion(str, Enum):
    DEFAULT = "{Cosmos DB ODBC Driver}"
