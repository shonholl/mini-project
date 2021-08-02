import json
import csv


order_status = ["payment pending","preparing","shipped","delivered"]

products_prices = [
            { "name": "water",
            "price":1.00},
            {"name": "coke",
            "price":1.40},
            {"name": "orange juice",
            "price":1.25}
        ]

couriers_numbers = [
            { "name": "Milo",
            "phone":"07861326754"},
            {"name": "Nova",
            "phone":"07456333821"},
            {"name": "Chris",
            "phone":"07539749203"}
        ]

try:
    with open('couriers.csv') as file:
        reader = csv.DictReader(file,delimiter= ',')

except FileNotFoundError as fnfe:
        print("Unable to open file:" + str(fnfe))

try:
    with open('products.csv') as file:
        reader = csv.DictReader(file,delimiter= ',')


except FileNotFoundError as fnfe:
        print("Unable to open file: " + str(fnfe))       

try:
    with open('orders.csv') as file:
        reader = csv.DictReader(file,delimiter= ',')

except FileNotFoundError as fnfe:
        print("Unable to open file: " + str(fnfe))



def main_menu():
    print("Main Menu Options")
    print("[0] Exit App")
    print("[1] Order")
    print("[2] Courier Menu")
    print("[3] Orders Menu")

def product_menu():
    print("Product Menu Options")
    print("[0] Return to Main Menu")
    print("[1] Order(Products List)")
    print("[2] New Product")
    print("[3] Update Product")
    print("[4] Delete Product")

def couriers_menu():
    print("Couriers Menu Options")
    print("[0] Return to Main Menu")
    print("[1] Couriers List")
    print("[2] New Courier")
    print("[3] Update Courier")
    print("[4] Delete Courier")

def order_menu():
    print("Order Menu Options")
    print("[0] Return to Main Menu ")
    print("[1] Orders List")
    print("[2] New Order")
    print("[3] Update Order Status")
    
while True:
    
    mainmenu = main_menu()
    main_menu_options = int(input("Please select a main menu option"))
    
    #products menu
    if main_menu_options == 1:
        productsmenu = product_menu()
        product_menu_options = int(input("Please select a product menu option"))
        if product_menu_options == 0:
            mainmenu = main_menu()
        
        elif product_menu_options == 1:
            print(products_prices)
            
        elif product_menu_options == 2:
            
            product_name = input("Enter name of product")
            product_price = float(input("Enter product price"))
            
            new_product = {"name": product_name,
                            "price" : product_price}
            
            products_prices.append(new_product)
            print(products_prices)
            
        elif product_menu_options == 3:
            print("index",":","value")
            for i,v in enumerate(products_prices):
                print(i,":",v)
            update_product_index = int(input("Select a product index to update"))
            new_product = input("Enter a new product")
            products_prices[update_product_index] = new_product
            print(products_prices)
            
        elif product_menu_options == 4:
            print("index",":","value")
            for i,v in enumerate(products_prices):
                print(i,":",v)
            delete_product_index = int(input("Select a product index to remove"))
            del products_prices[delete_product_index]
            print(products_prices)
    
    #couriers menu
    elif main_menu_options == 2:
        couriermenu = couriers_menu()
        courier_menu_options = int(input("Please select a courier menu option"))
    
        if courier_menu_options == 0:
            mainmenu = main_menu()
            
        elif courier_menu_options == 1:
            print(couriers_numbers)
            
        elif courier_menu_options == 2:
            
            courier_name = input("Enter name of courier")
            courier_phone_number = int(input("Enter courier phone number"))
            
            new_courier = {"name": courier_name,
                            "phone" : courier_phone_number}
            
            couriers_numbers.append(new_courier)
            print(couriers_numbers)
        
        elif courier_menu_options == 3:
            print("index",":","value")
            for i,v in enumerate(couriers_numbers):
                print(i,":",v)
            courier_index = int(input("Select a courier index to update"))
            new_courier = input("Enter a new courier")
            couriers_numbers[courier_index] = new_courier
            print(couriers_numbers)
            
        elif courier_menu_options == 4:
            print("index",":","value")
            for i,v in enumerate(couriers_numbers):
                print(i,":",v)
            courier_index = int(input("Select a courier index to remove"))
            del couriers_numbers[courier_index]
            print(couriers_numbers)
    
    #orders menu
    elif main_menu_options == 3:
        ordermenu = order_menu()
        order_menu_options = int(input("Please select an order menu option"))
    
        if order_menu_options == 0:
            mainmenu = main_menu()
        
        elif order_menu_options == 1:
            try:
                with open('orders.json','r') as orders_file:
                    orders_dict = json.load(orders_file)
                    print(orders_dict)
            except FileNotFoundError as fnfe:
                print("Unable to open file: " + str(fnfe)) 
        
        elif order_menu_options == 2:
            customer_name = input("Enter your name")
            customer_address = input("Enter your address")
            customer_phone = input("Enter your contact number")
            
            print("index",":","value")
            for i,v in enumerate(products_prices):
                print(i,":",v)
            product_ID = [int(product_ID) for product_ID in 
                        input("Please add product(s) to basket:").split(",")]
            print(product_ID)
            
            print("index",":","value")
            for i,v in enumerate(couriers_numbers):
                print(i,":",v)
            courier_index = int(input("Select courier index"))
            order_status = "preparing"
            
            new_order = {
                        "customer_name": customer_name,
                        "customer_address": customer_address,
                        "customer_phone": customer_phone,
                        "courier": courier_index,  
                        "status": order_status,
                        "items" : product_ID
                        }
            
            try:
                with open('orders.json','r') as orders_file:
                    orders_dict = json.load(orders_file)
                    
                orders_dict["order_menu"].append(new_order)
                    
                with open('orders.json','w') as write_file:
                    json.dump(orders_dict,write_file,indent=4)
        
                print(orders_dict)
                    
            except FileNotFoundError as fnfe:
                print("Unable to open file: " + str(fnfe)) 
        
        elif order_menu_options == 3:
            
            orders_list = [
            {
            "customer_name": "Ethan",
            "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
            "customer_phone": "0789887334",
            "courier": 0,
            "status": "preparing",
            "items": [0]
        },
        {
            "customer_name": "Julia",
            "customer_address": "14 Ladbroke Cresecent, LONDON, W16 8UI",
            "customer_phone": "07562223987",
            "courier": 1,
            "status": "shipped",
            "items":[1,2]
        },
        {
            "customer_name": "Artie",
            "customer_address": "Flat 8, Roman Way, Richmond, KT2 5LV",
            "customer_phone": "07136547815",
            "courier": 2,
            "status": "pending payment",
            "items" :[1]
        },
        {
            "customer_name": "Marleigh",
            "customer_address": "79 Sycamore Drive, Kew, SW14 0NY ",
            "customer_phone": "0762434991",
            "courier": 3,
            "status": "delivered",
            "items":[2,0]
        }
    ]
    
        print(f" index 0:",orders_list[0])
        print(f"index 1:",orders_list[1])
        print(f" index 2:",orders_list[2])
        print(f"index 3:",orders_list[3])
        order_index = int(input("Please select an order to update"))
        
        print("index",":","value")
        for i,v in enumerate(order_status):
                print(i,":",v)
        order_status_index = int(input("Please select a order status index"))
        
        new_order_status = input("Please enter a new order status")    
    
        orders_list[order_status_index]["status"] = new_order_status 
        
        print(orders_list)     
    
    
    
                
    

#exit app
    elif main_menu_options == 0:
        
        fieldnames_couriers = ['name','phone']
        
        try:
            with open('couriers.csv',mode='w') as couriers_file:
                writer = csv.DictWriter(couriers_file,fieldnames=fieldnames_couriers)
                
                writer.writeheader()
                writer.writerows(couriers_numbers)
                
        except FileNotFoundError as fnfe:
            print("Unable to open file:" + str(fnfe))
        
        
        
        fieldnames_products = ['name','price']
        
        try:
            
            with open('products.csv',mode='w') as products_file:
                    writer = csv.DictWriter(products_file,fieldnames= fieldnames_products)
                
                    writer.writeheader()
                    writer.writerows(products_prices)
                    
        except FileNotFoundError as fnfe:
            print("Unable to open file: " + str(fnfe))       
        
        
        fieldnames_orders = ['customer_name','customer_address',
                            'customer_phone','courier','status']
        
        orders = [
            {
            "customer_name": "Ethan",
            "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
            "customer_phone": "0789887334",
            "courier": 0,
            "status": "preparing",
            "items": [0]
        },
        {
            "customer_name": "Julia",
            "customer_address": "14 Ladbroke Cresecent, LONDON, W16 8UI",
            "customer_phone": "07562223987",
            "courier": 1,
            "status": "shipped",
            "items":[1,2]
        },
        {
            "customer_name": "Artie",
            "customer_address": "Flat 8, Roman Way, Richmond, KT2 5LV",
            "customer_phone": "07136547815",
            "courier": 2,
            "status": "pending payment",
            "items" :[1]
        },
        {
            "customer_name": "Marleigh",
            "customer_address": "79 Sycamore Drive, Kew, SW14 0NY ",
            "customer_phone": "0762434991",
            "courier": 3,
            "status": "delivered",
            "items":[2,0]
        }
    ]
        
        try:
            
            with open('orders.csv',mode='w') as orders_file:
                    writer = csv.DictWriter(orders_file,fieldnames= fieldnames_orders)
                
                    writer.writeheader()
                    writer.writerows(orders)
                    
        except FileNotFoundError as fnfe:
            print("Unable to open file: " + str(fnfe)) 
        
        print("See you next time")
        break
        
    
        
    else:
        print("Invalid input")