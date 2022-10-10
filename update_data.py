#!/usr/bin/python3

import sqlite3
import display_all

connection = sqlite3.connect("store.db")
cVar = connection.cursor()

#cVar.execute("""DROP TABLE store""");
#connection.commit()

display_all

def update_data():

    item = input("Choose an item to update: ")

    cVar.execute("SELECT * FROM store_items WHERE item_name = ?", (item,))
    data = cVar.fetchall()

    if len(data)==0:
            print("There is no item named %s"%item)
    else:
            print("Item %s found"%item + "\n")
            
            #print initial item info
            #print_item(item)
            

            cVar.execute("SELECT item_id FROM store_items WHERE item_name = ?", (item,))
            cur_id = cVar.fetchall()

            field = input("Choose one field to update (id/name/price): ")

            if field=='id':
                
                new_id = input("Enter the new id for item " + item + ": ")
                cVar.execute("UPDATE store_items SET item_id = ? WHERE item_name = ?", (new_id, item))

                print("New id for item " + item + " is " + new_id)

                connection.commit()
                
    
            elif field=='name':
                new_name = input("Enter the new name for item " + item + ": ")
                cVar.execute("UPDATE store_items SET item_name = ? WHERE item_name = ?", (new_name, item))

                print("New name for item " + item + " is " + new_name)

                connection.commit()
                

            elif field=='price':
                new_price = input("Enter the new price for item " + item + ": ")
                cVar.execute("UPDATE store_items SET item_price = ? WHERE item_name = ?", (new_price, item))

                print("New price for item " + item + " is " + new_price)

                connection.commit()
                

            else:
                print("Invalid input")
                
    exit(0)            

update_data()
