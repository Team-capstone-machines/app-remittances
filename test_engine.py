#!/usr/bin/python3
import urllib
from sqlalchemy import create_engine
from models.receiver import Receiver, Base
from sqlalchemy.orm.session import Session
import pyodbc
server = 'remittances.database.windows.net'
database = 'remittances_db'
username = 'remittances_user'
password = 'DUXowU%$dBmB'
driver = '{ODBC Driver 13 for SQL Server}'
odbc_string = r'Driver={ODBC Driver 17 for SQL Server};Server=tcp:remittances.database.windows.net,1433;Database=remittances_db;Uid=remittances_user;Pwd=DUXowU%$dB\
mB;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
connect_str = 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus(odbc_string)
engine = create_engine(connect_str, echo=True)
print(engine.table_names())
""" Base.metadata.create_all(engine)
session = Session(bind=engine)
query = session.query(Receiver).all()
print(query) """