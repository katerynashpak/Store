#!/usr/bin/python3


import sqlite3

def display():

    connection = sqlite3.connect("store.db")
    cVar = connection.cursor()


    cVar.execute("SELECT * FROM store_items")
    obj = cVar.fetchall()

    row_count = len(obj)
    print ("ID        ", "Item Name             ", "Price    ")
    print ("............................................................")
    i = 0
    while i < row_count:
        print (obj[i][0]," "*(12-len(obj[i])), obj[i][1]," "*(12-len(obj[i][1])), " "*(12-len(obj[i])), "$",obj[i][2]," "*(12-len(str(obj[i][2]))))
        i=i+1

    connection.close()


display()
