'''
Function will be used to add new customer to database
'''

import sqlite3
import os
from sqlite3.dbapi2 import Cursor, Row, converters
import sys
from time import sleep
from clear import clear
from datetime import date
from new_customer import new_customer

def check_db(filename):
    return os.path.exists(filename)

db_file = 'thisAPP1.db'

if check_db(db_file):
    print('Connected to database')

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
#sleep(2)
clear()

def customer_check():
    sname = input('Customer\' Surname: ')

    
    #check if customer is in database
    data = cursor.execute("SELECT * FROM customers WHERE surname=?;", [sname]).fetchone()
    #if found ask if display details
    if data is not None:
        while True:
            try:
                yn1 = input('Show Details?\nY or N')
                yn1 = yn1.upper()
                if yn1 == 'Y':
                    print('hell yes')
                    break
                elif yn1 =='N':
                    print('hell no')
                    break
                else:
                    print('Choose Y or N')
            except Exception as e:
                continue
    #if not found ask if add the details
         else:
    


    


    #if yes get new details


    #if not go back to start





customer_check()
conn.close()