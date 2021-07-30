import json
import csv

products_list = ['water','coke','orange juice']

couriers_list = ['Milo','Nova','Chris']

order_status = ["payment pending","preparing","shipped","delivered"]

try:
    with open('couriers.csv') as file:
        reader = csv.DictReader(file,delimiter= ',')
        # for row in reader:
        #     print(row)

except FileNotFoundError as fnfe:
        print("Unable to open file:" + str(fnfe))

try:
    with open('products.csv') as file:
        reader = csv.DictReader(file,delimiter= ',')
        # for row in reader:
        #     print(row)

except FileNotFoundError as fnfe:
        print("Unable to open file: " + str(fnfe))       

try:
    with open('orders.csv') as file:
        reader = csv.DictReader(file,delimiter= ',')
        # for row in reader:
        #     print(row)

except FileNotFoundError as fnfe:
        print("Unable to open file: " + str(fnfe))


def main_menu():
    print("main_menu_options")
    print("[0] Exit App")
    print("[1] Order")
    print("[2] Courier menu")
    print("[3] Orders menu")

def product_menu():
    print("product_menu_options")
    print("[0] Return to main menu")
    print("[1] Drinks")
    print("[2] Custom drink")
    print("[3] Update drink")
    print("[4] Delete drink")

def couriers_menu():
    print("couriers_menu_options")
    print("[0] Return to main menu")
    print("[1] Couriers list")
    print("[2] Custom courier")
    print("[3] Update courier")
    print("[4] Delete courier")

def order_menu():
    print("order_menu_options")
    print("[0] Return to main menu ")
    print("[1] Orders dictionary")
    print("[2] Customer and courier details")
    print("[3] Update order status")
    
while True:
    
    mainmenu = main_menu()
    main_menu_options = int(input("Please select a main menu option"))
    
    #products menu
    if main_menu_options == 1:
        products = product_menu()
        product_menu_options = int(input("Please select a product menu option"))
        if product_menu_options == 0:
            mainmenu = main_menu()
        
        elif product_menu_options == 1:
            print(products_list)
            
        elif product_menu_options == 2:
            custom_drink = input("Please select another drink")
            products_list.append(custom_drink)
            
        elif product_menu_options == 3:
            print("index",":","value")
            for i,v in enumerate(products_list):
                print(i,":",v)
            update_drink_index = int(input("Please select a drink index to update"))
            new_drink = input("Please enter a new drink")
            products_list[update_drink_index] = new_drink
            print(products_list)
            
        elif product_menu_options == 4:
            print("index",":","value")
            for i,v in enumerate(products_list):
                print(i,":",v)
            delete_drink_index = int(input("Please select a drink index to remove"))
            del products_list[delete_drink_index]
            print(products_list)
    
    #couriers menu
    elif main_menu_options == 2:
        couriermenu = couriers_menu()
        courier_menu_options = int(input("Please select a courier menu option"))
    
        if courier_menu_options == 0:
            mainmenu = main_menu()
            
        elif courier_menu_options == 1:
            print(couriers_list)
            
        elif courier_menu_options == 2:
            custom_courier = input("Please enter a new courier")
            couriers_list.append("new_courier")
            print(custom_courier)
        
        elif courier_menu_options == 3:
            print("index",":","value")
            for i,v in enumerate(couriers_list):
                print(i,":",v)
            courier_index = int(input("Please select a courier index to update"))
            new_courier = input("Please enter a new courier")
            couriers_list[courier_index] = new_courier
            print(couriers_list)
            
        elif courier_menu_options == 4:
            print("index",":","value")
            for i,v in enumerate(couriers_list):
                print(i,":",v)
            courier_index = int(input("Please select a courier index to remove"))
            del couriers_list[courier_index]
            print(couriers_list)
    
    #orders menu
    elif main_menu_options == 3:
        ordermenu = order_menu()
        order_menu_options = int(input("Please select an order option"))
    
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
            for i,v in enumerate(couriers_list):
                print(i,":",v)
            courier_index = int(input("Please select courier index"))
            order_status = "preparing"
            
            new_order = {
                        "customer_name": customer_name,
                        "customer_address": customer_address,
                        "customer_phone": customer_phone,
                        "courier": courier_index,  
                        "status": order_status
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
                "customer_name": "Tommy",
                "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
                "customer_phone": "0789887334",
                "courier": 0,
                "status": "preparing"
            },
            {
                "customer_name": "John",
                "customer_address": "14 Ladbroke Street, LONDON, W16 8UI",
                "customer_phone": "07562223987",
                "courier": 1,
                "status": "shipped"
            },
            {
                "customer_name":"Arthur",
                "customer_address": "Flat 8, Roman way, Richmond, KT2 5LV",
                "customer_phone": "07136547815",
                "courier": 2,
                "status": "pending payment"
            },
            {
                "customer_name":"Michael",
                "customer_address": "79 Sycamore Drive, Kew, SW14 0NY ",
                "customer_phone": "0762434991",
                "courier": 3,
                "status": "delivered"
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
        
        couriers = [
            { "name": "Milo",
            "phone":"07861326754"},
            {"name": "Nova",
            "phone":"07456333821"},
            {"name": "Chris",
            "phone":"07539749203"}
        ]
        
        try:
            with open('couriers.csv',mode='w') as couriers_file:
                writer = csv.DictWriter(couriers_file,fieldnames=fieldnames_couriers)
                
                writer.writeheader()
                writer.writerows(couriers)
                
        except FileNotFoundError as fnfe:
            print("Unable to open file:" + str(fnfe))
        
        
        
        fieldnames_products = ['name','price']
        
        products = [
            { "name": "water",
            "price":1.00},
            {"name": "coke",
            "price":1.40},
            {"name": "orange juice",
            "price":1.25}
        ]
        
        try:
            
            with open('products.csv',mode='w') as products_file:
                    writer = csv.DictWriter(products_file,fieldnames= fieldnames_products)
                
                    writer.writeheader()
                    writer.writerows(products)
                    
        except FileNotFoundError as fnfe:
            print("Unable to open file: " + str(fnfe))       
        
        
        fieldnames_orders = ['customer_name','customer_address',
                            'customer_phone','courier','status']
        
        orders = [
            {
                "customer_name": "Tommy",
                "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
                "customer_phone": "0789887334",
                "courier": 0,
                "status": "preparing"
            },
            {
                "customer_name": "John",
                "customer_address": "14 Ladbroke Street, LONDON, W16 8UI",
                "customer_phone": "07562223987",
                "courier": 1,
                "status": "shipped"
            },
            {
                "customer_name":"Arthur",
                "customer_address": "Flat 8, Roman way, Richmond, KT2 5LV",
                "customer_phone": "07136547815",
                "courier": 2,
                "status": "pending payment"
            },
            {
                "customer_name":"Michael",
                "customer_address": "79 Sycamore Drive, Kew, SW14 0NY ",
                "customer_phone": "0762434991",
                "courier": 3,
                "status": "delivered"
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