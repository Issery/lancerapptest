from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import urllib


CONFIG_URL = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:test1-server.database.windows.net;Database=test1database;Uid=lancer;Pwd=Lrd19970323;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
params = urllib.parse.quote_plus(CONFIG_URL)
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
print('params:\n{}\nconn_str:\n{}'.format(params,conn_str))

engine = create_engine(conn_str,echo=True,convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
print(type(Base))
print('--------------------------------------------')
def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)