#!/usr/bin/python3
from datetime import datetime
import sqlite3
import sys
import os



connection = sqlite3.connect("store.db")
cVar = connection.cursor()

#----------------------Calculate Total Price---------------------------------

def calc_total(data1):
    cVar.execute("SELECT SUM(item_price) FROM cart")
    total = cVar.fetchone()
    print("Total: $",round(total[0], 2))


#-----------------------Display the Cart to the User--------------------------------


def display_cart(data1):
    print("")
    print("                         YOUR CART:                          ")
    print(".............................................................")
    #print(data1)

    row_count = len(data1)
    print ("ID          ", "Item Name         ", "Price    ")
    print ("............................................................")
    i = 0
    while i < row_count:
        print (data1[i][0]," "*(12-len(data1[i])), data1[i][1]," "*(12-len(data1[i][1]))," "*(12-len(data1[i])), "$",data1[i][2]," "*(12-len(str(data1[i][2]))))
        i=i+1
    print("\n")

#-----------------------Write Cart/Purchase to File--------------------------------

def to_file(data1):
    file_path = 'purchase_history.txt'
    sys.stdout = open(file_path, "a")

    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
    
    print("\n")
    print("Purchase made on ", dt_string)
    display_cart(data1)
    calc_total(data1)


#--------------------------Main-----------------------------


while True:


    item = input("Choose an item to purchase: ")

    cVar.execute("SELECT * FROM store_items WHERE item_name = ?", (item,))
    data = cVar.fetchall()



    if len(data)==0:
            print('There is no item named %s'%item)
    else:
            print('Item %s found'%item)

            #print(data)
            cVar.execute("INSERT INTO cart SELECT * FROM store_items WHERE item_name = ?", (item,))
            cVar.execute("SELECT * FROM cart")
            data1 = cVar.fetchall()
            #print(data1)

            cont = input("Another one? [y/n] ")
            if cont == "n":
                display_cart(data1)
                calc_total(data1)
                mod = input("Ready to pay? [y/n] ")
                if mod == "y":
                    print("Thank you for your purchase! See you soon!")
                    #write to file with current date
                    to_file(data1)

                elif mod == "n":
                    continue

                break
    
#-------------------------------------------------------


connection.close()




