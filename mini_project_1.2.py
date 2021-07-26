import json

products_list = ['water','coke','orange juice']

couriers_list = ['Tommy','Arthur','John','Michael','Finn']

order_status = ["payment pending","preparing","shipped","delivered"]

try:
    with open('couriers.txt','r') as couriers_file:
        couriers = couriers_file.read()
        print(couriers)
except Exception as e:
    print("An error has occured:" + str(e))

try:
    with open('products.txt','r') as products_file:
        products = products_file.read()
        print(products)
except Exception as e:
    print("An error has occured:" + str(e))




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
                    
                    orders_dict["orders_menu"].append(new_order)
            
                with open('orders.json','a') as write_file:
                    json.dump(new_order,write_file,indent = 4)
                    print(orders_dict)
                    
            except FileNotFoundError as fnfe:
                print("Unable to open file: " + str(fnfe)) 
                
    
    #exit app
    elif main_menu_options == 0:
        try:
            with open('couriers.txt','w') as couriers_file:
                for courier in couriers_list:
                    couriers_file.write(courier + '\n')
        except FileNotFoundError as fnfe:
            print("Unable to open file:" + str(fnfe))
        
        try:
            with open('products.txt','w') as products_file:
                for product in products_list:
                    products_file.write(product + '\n')
        except FileNotFoundError as fnfe:
            print("Unable to open file: " + str(fnfe))        
        
        print("See you next time")
        break
        
    
        
    else:
        print("Invalid input")