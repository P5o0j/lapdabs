"""Initial form checking if car is already in database or if need to be added"""

import sqlite3
import os
import datetime

#connect to database
def check_db(filename):
    return os.path.exists(filename)

db_file = 'thisAPP.db'

if check_db(db_file):
    print('Connected to database')
    sys.exit(0)


#get vrn
def vrn_check():
    vrn = input('Registration Number: ')
    vrn = vrn.upper()


#check if entry is in database
with sqlite3.connect(db_file) as conn:
    conn.executescript('SELECT vrn FROM CARS WHERE code=?', vrn)


#if entry is in database show details



#ask if details are correct/ if not allow user to edit them 



#if entry not in database insert new line



