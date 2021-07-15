couriers_list = ['Tommy','Arthur','John','Michael','Finn']

# file = open('couriers.txt','w')
# for courier in couriers_list:
#     file.write(courier + '\n')
#     print(courier)


# products = ['water','orange juice','coke']

# file = open('products.txt','w')
# for product in products:
#     file.write(product + '\n')
#     print(product)

#courier menu

def couriers():
    print("couriers_menu_options")
    print("[0] Return to main menu")
    print("[1] Couriers list")
    print("[2] Custom courier")
    

couriers()

while True:
    

    courier_menu_option = input("Select an option")
    
    if courier_menu_option == '0':
        print(couriers()) #change to main_menu()
    elif courier_menu_option == '1':
        print(couriers_list)
    elif courier_menu_option == '2':
        custom_courier = input("Please add a new courier")
    couriers_list.append("new_courier")
    print(custom_courier)
        