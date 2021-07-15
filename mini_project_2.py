products_list = ['water','coke','orange juice']

def main_menu():
    print("main_menu_options")
    print("[0] Exit App")
    print("[1] Order")

def product_menu():
    print("product_menu_options")
    print("[0] Return to main menu")
    print("[1] Drinks")
    print("[2] Custom drink")

main_menu()

while True:

    
    main_menu_options = input("Select an option")
    
    if main_menu_options == '0':
        print("See you next time")
        #break
    elif main_menu_options == '1':
        product_menu()
        #continue
    else: 
        print("Invalid option")
        
    product_menu_options = input("Select an option")
    if product_menu_options == '0':
        print(main_menu())
        #Return to main menu
    elif product_menu_options == '1':
        print(products_list)
    elif product_menu_options == 2:
        custom_drink = input("Please select another drink")
    products_list.append("new_drink")
    #print(products_list)
    
        
#product_menu()    
    
    
