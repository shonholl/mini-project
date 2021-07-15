# order menu
order_status = ["payment pending","preparing","shipped","delivered"]

orders_list_dict = [
            {
                "customer_name": "Tommy",
                "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
                "customer_phone": "0789887334",
                "courier": "2",
                "status": "preparing"
            },
            {
                "customer_name": "John",
                "customer_address": "14 Ladbroke Street, LONDON, W16 8UI",
                "customer_phone": "07562223987",
                "courier": "1",
                "status": "shipped"
            },
            {
                "customer_name":"Arthur",
                "customer_address": "Flat 8, Roman way, Richmond, KT2 5LV",
                "customer_phone": "07136547815",
                "courier": "3",
                "status": "pending payment"
            },
            {
                "customer_name":"Michael",
                "customer_address": "79 Sycamore Drive, Kew, SW14 0NY ",
                "customer_phone": "0762434991",
                "courier": "2",
                "status": "delivered"
            }
        ]

def order_menu():
    print("order_menu_options")
    print("[0] Return to main menu ")
    print("[1] Orders dictionary")
    print("[2] Customer and courier details")
    print("[3] Update order status")
    
order_menu()

while True:
    order_menu_option = input("Select an option")
    
    #elif courier_menu_option == 3:
    
    if order_menu_option == '0':
        print(order_menu()) #change to main menu
    elif order_menu_option == '1':
        print(orders_list_dict)
    elif order_menu_option == '2':
        customer_name = input("Enter your name")
        customer_address = input("Enter your address")
        customer_phone = input("Enter your contact number")
        