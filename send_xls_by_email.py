import platform
import cx_Oracle
import configparser
import sys
import os

from datetime import date, datetime
# import xlsxwriter

from ftplib import FTP
from pathlib import Path

# import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from subprocess import Popen, PIPE

# Read Oracle.ini file and get variables
parser = configparser.ConfigParser()
if platform.system() == 'Windows':
    parser.read(env_ctl + 'pythonOracle.ini.MI')
else:
    parser.read(env_ctl + 'pythonOracle.ini')
db_username = parser['database']['username']
db_password = parser['database']['password']
db_host = parser['database']['host']
db_port = parser['database']['port']
db_sid = parser['database']['sid']

dsn_tns = cx_Oracle.makedsn(db_host, db_port, db_sid)
conn = cx_Oracle.connect(user=db_username, password=db_password, dsn=dsn_tns, encoding="UTF-8", nencoding="UTF-8")



def sql_select(fetch_type, sql, default_params=[], assoc=0):
    cur = conn.cursor()
    cur.execute(sql, default_params)
    if assoc == 1:
        columns = [col[0] for col in cur.description]
        cur.rowfactory = lambda *args: dict(zip(columns, args))
    while True:
        if fetch_type == 'one':
            row = cur.fetchone()
        else:
            row = cur.fetchall()
        cur.close()
        if row is None:
            return None
        else:
            return row


# ----------------------------------------------------------------------------------------------------------------------
def main():
    print('')


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
