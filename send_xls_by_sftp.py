import platform
import configparser
import sys
import os

from datetime import date, datetime
# import xlsxwriter

from ftplib import FTP
from pathlib import Path


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
