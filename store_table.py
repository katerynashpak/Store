#!/usr/bin/python3

import sqlite3

connection = sqlite3.connect("store.db")
cVar = connection.cursor()


cVar.execute("""DROP TABLE IF EXISTS store_items""")
connection.commit()



sql1 = """CREATE TABLE store_items(
    item_id INTEGER PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    item_price INT NOT NULL,
    UNIQUE(item_id, item_name, item_price)
    );"""


sql2 = """CREATE TABLE cart(
    item_id INTEGER PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    item_price INT NOT NULL,
    UNIQUE(item_id, item_name, item_price)
    );"""

cVar.execute(sql1)
cVar.execute(sql2)


connection.close()

