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



def new_customer():

    #bulid customer code
    dataset=cursor.execute("SELECT COUNT(*) FROM temp_customer")
    count = dataset.fetchall()
    nextSeq = int(count[0][0]) + 1 
    #nextSeq = int(seq) + 1
    cuscde = "C" + str(nextSeq)
    #print(cuscde)

    #get date when entry was added
    dateAdd = date.today()

    #get regnum
    while True:
        vrn = input('Reg number: ')
        if vrn:
            break
        else:
            print('Mandatory field')

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
            company = None
            break
        break
    #get address line 1
    while True:
        addrl1 = input('Address: ')
        if addrl1:
            break
        else:
            print('Mandatory field')

    #get address line 2
    while True:
        addrl2 = input('Address: ')
        if addrl2 == '':
            addrl2 = None
            break
        break

    #get address line 3
    while True:
        addrl3 = input('Address: ')
        if addrl3 == '':
            addrl3 = None
            break
        break

    #get postcode
    while True:
        postcode = input('Postcode: ')
        if postcode:
            break
        else:
            print('Mandatory field')

    #get city
    while True:
        city = input('City: ')
        if city:
            break
        else:
            print('Mandatory field')

    #get phone number
    while True:
        phonum = input('Phone number: ')
        if phonum:
            break
        else:
            print('Mandatory field')

    #get email
    while True:
        email = input('Email address: ')
        if email == '':
            email = None
            break
        break

    #insert data to database
    cursor.execute("INSERT INTO temp_customer values (?,?,?,?,?,?,?,?,?,?,?,?,?);", 
                   (cuscde, dateAdd, vrn.upper(), name.capitalize(), surname.capitalize(), company, addrl1, addrl2, addrl3, postcode.upper(), city.capitalize(), phonum, email ))
    conn.commit()



    #print(dateAdd)

    
customer()
conn.close()