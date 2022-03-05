'''
Function will be used to add new customer to database
'''

import sqlite3
import os
import datetime
from sqlite3.dbapi2 import Cursor, Row, converters
import sys
from time import sleep
from clear import clear
import datetime

def check_db(filename):
    return os.path.exists(filename)

db_file = 'thisAPP1.db'

if check_db(db_file):
    print('Connected to database')

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
#sleep(2)
clear()

def customer():
