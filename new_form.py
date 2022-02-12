"""Initial form checking if car is already in database or if need to be added"""

import sqlite3
import os
import datetime
#from sqlite3.dbapi2 import converters
import sys
from time import sleep
from clear import clear

#connect to database
def check_db(filename):
    return os.path.exists(filename)

db_file = 'thisAPP.db'

if check_db(db_file):
    print('Connected to database')

conn = sqlite3.connect(db_file)
sleep(2)
clear()

#get vrn
def vrn_exist():
    vrn = input('Registration Number: ')
    vrn = vrn.upper()




#check if entry is in database
    for row in conn.execute("SELECT * FROM vw_vehicles WHERE regnum= ?", [vrn]):
        print(row)
        return True

#if entry is in database show details
        if row == True:
            print("Car in db")


#ask if details are correct/ if not allow user to edit them 



#if entry not in database insert new line



#close database connection
vrn_exist()
conn.close()