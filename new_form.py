"""Initial form checking if car is already in database or if need to be added"""

import sqlite3
import os
import datetime

#connect to database
def check_db(filenamde):
    return os.path.exists(filename)

db_file = 'thisAPP.db'

if check_db(db_file):
    print('Connected to database')
    sys.exit(0)


#get vrn



#check if entry is in database
with sqlite3.connect(db_file) as conn:
    conn.executescript("""
    
    """)


#if entry is in database show details



#ask if details are correct/ if not allow user to edit them 



#if entry not in database insert new line


