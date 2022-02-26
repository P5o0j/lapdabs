"""Initial form checking if car is already in database or if need to be added"""

import sqlite3
import os
import datetime
from sqlite3.dbapi2 import Cursor, Row, converters
import sys
from time import sleep
from clear import clear
from car_details import car_details


#connect to database
def check_db(filename):
    return os.path.exists(filename)

db_file = 'thisAPP.db'

if check_db(db_file):
    print('Connected to database')

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
#sleep(2)
clear()
  
#get vrn
def vrn_exist():
    vrn = input('Registration Number: ')
    vrn = vrn.upper()


#check if vrn is in database
    data = cursor.execute("SELECT * FROM vw_vehicles WHERE regnum=?;", [vrn]).fetchone()
    if data is not None:
        #show car details
        car_details(row)
    else:
        print('Car not in db. Would you like to add it?')
            

#ask if details are correct/ if not allow user to edit them 
        



#if entry not in database insert new line
    
            


#close database connection
vrn_exist()
conn.close()