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

    #bulid customer code
    dataset=cursor.execute("SELECT COUNT(*) FROM customer")
    count = dataset.fetchall()
    cuscde = "C" + str(count[0][0])

    #get date when entry was added
    dateAdd = date.today()

    #get regnum

    #get name
    while True:
        name = input('Owner name: ')
        if name:
            break
        else:
            print('Mandatory field')

    #get surname
    while True:
        surname = input('Owner Surname: ')
        if surname:
            break
        else:
            print('Mandatory field')

    ##get company name
    while True:
        company = input('Company name: ')
        if company == '':
            break
        break
    #get address

    #get phone number
    while True:
        phonum = str(input('Phone number: '))
        if phonum:
            break
        else:
            print('Mandatory field')

    #get email

    #insert data to database



    print(dateAdd)

    
customer()