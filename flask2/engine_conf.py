import urllib
import pyodbc
from sqlalchemy import create_engine

s1 = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:test1-server.database.windows.net;Database=test1database;Uid=lancer;Pwd=Lrd19970323;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
params = urllib.parse.quote_plus(s1)
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
engine_azure = create_engine(conn_str,echo=True)

print('connection is ok')
# print(engine_azure.table_names())
