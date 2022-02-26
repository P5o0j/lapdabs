'''
Function will be used to add new car to database in situation where initial form won't return any rows from search
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

def car_insert():
    vrn = input('Registration Number: ')
    #print(f"Registration number : {vrn}")
    #fname = input('Owner name: ')
    #sname = input('Owner Surname: ')
    make = input('Make: ')
    model = input('Model: ')
    colour = input('Colour: ')

    #check for correct fuel type
    while True:
        try:
            fuel = input('Fuel Type: ')
            if fuel == 'diesel':
                fuel = 'F001'
                break
            elif fuel == 'petrol':
                fuel = 'F002'
                break
        except Exception as e:
            print('Error', e)
            print('Wrong type')
            continue
    #check if millage is passed as integer
    while True:
        try:
            milage = int(input('Milage: '))
            break
        except ValueError:
            print('Wrong value')
            continue
    mot = input('MOT due date: ')

    cursor.execute("INSERT INTO temp_veh values (?,?,?,?,?,?,?);", (vrn.upper(), make.capitalize(), model.capitalize(), fuel, milage, colour, mot ))
    conn.commit()

    print('Car added to database')

car_insert()
conn.close()
