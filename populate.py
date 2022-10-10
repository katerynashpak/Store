#!/usr/bin/python3

import sqlite3

connection = sqlite3.connect("store.db")
cVar = connection.cursor()

def dynamic_data():
    item_id = int(input("Item ID: "))
    item_name = input("Item Name: ")
    item_price = float(input("Item Price: "))

    cVar.execute("INSERT INTO store_items (item_id, item_name, item_price) VALUES (?,?,?)", (item_id, item_name, item_price))
    connection.commit()


numOf_Items = int(input("Enter a number of items you'd like to add to the store: "))

for i in range(0, numOf_Items):
    print("--------Item", i+1, "--------")
    dynamic_data()


connection.close()




