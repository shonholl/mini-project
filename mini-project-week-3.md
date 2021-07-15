# Mini Project Week 3

So far we've been using one-dimensional lists of data, however, this won't work for orders. We need to store more information such as the customer's name, address and phone number, as well as the status of the order, the courier etc. To solve this we'll use a two-dimensional data structure, a `dictionary`. We won't be able to read/write this structure to text file anymore, but we'll fix this later. For now we'll also skip adding products to the order.

We'll also write a unit test that covers the update order status functionality.

## Goals

As a user I want to:

- create a product, courier, or order and add it to a list
- view all products, couriers, or orders
- update the status of an order
- persist my data
- _STRETCH_ update or delete a product, order, or courier

## Spec

- A `product` should just be a `string` containing its name, i.e: `"Coke Zero"`
- A list of `products` should be a list of `strings`, i.e: `["Coke Zero"]`
- A `courier` should just be a `string` containing its name, i.e: `"John"`
- A list of `couriers` should be a list of `strings`, i.e: `["John"]`
- An `order` should be a `dict`, i.e:

```json
{
  "customer_name": "John",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "courier": 2,
  "status": "preparing"
}
```

- A list of `orders` should be a list of `dicts`, i.e: `[{...},{...}]`
- Data should be persisted to a `.txt` file on a new line for each `courier` or `product`, ie:

```txt
John
Claire
```

## Pseudo Code

```txt
LOAD products list from products.txt
LOAD couriers list from couriers.txt
CREATE orders list of dictionaries      # WEEK 3 UPDATE
CREATE order status list                # WEEK 3 UPDATE

PRINT main menu options
GET user input for main menu option

IF user input is 0:
    SAVE products list to products.txt
    SAVE couriers list to couriers.txt
    EXIT app

# products menu
ELSE IF user input is 1:
    PRINT product menu options
    GET user input for product menu option

    IF user inputs 0:
        RETURN to main menu

    ELSE IF user input is 1:
        PRINT products list

    ELSE IF user input is 2:
        # CREATE new product
        GET user input for product name
        APPEND product name to products list

    ELSE IF user input is 3: 
        # STRETCH GOAL - UPDATE existing product

        PRINT product names with its index value
        GET user input for product index value
        GET user input for new product name
        UPDATE product name at index in products list

    ELSE IF user input is 4:
        # STRETCH GOAL - DELETE product
        
        PRINT products list
        GET user input for product index value
        DELETE product at index in products list

# couriers menu
ELSE IF user input is 2:
    PRINT courier menu options
    GET user input for courier menu option

    IF user inputs 0:
        RETURN to main menu

    ELIF user inputs 1:
        PRINT couriers list

    ELSE IF user input is 2:
        # CREATE new courier
        GET user input for courier name
        APPEND courier name to couriers list

    ELSE IF user input is 3: 
        # STRETCH GOAL - UPDATE existing courier

        PRINT courier names with its index values
        GET user input for courier index value
        GET user input for new courier name
        UPDATE courier name at index in couriers list

    ELSE IF user input is 4:
        # STRETCH GOAL - DELETE courier
            
        PRINT courier list
        GET user input for courier index value
        DELETE courier at index in courier list

# orders menu - WEEK 3 UPDATE
ELSE IF user input is 3:
    IF user input is 0:
        RETURN to main menu

    ELSE IF user input is 1:
        PRINT orders dictionary

    ELSE IF user input is 2:
        GET user input for customer name
        GET user input for customer address
        GET user input for customer phone number

        PRINT couriers list with index value for each courier
        GET user input for courier index to select courier
        SET order status to be 'PREPARING'
        APPEND order to orders list

    ELSE IF user input is 3:
        # UPDATE existing order status

        PRINT orders list with its index values
        GET user input for order index value

        PRINT order status list with index values
        GET user input for order status index value
        UPDATE status for order

    ELSE IF user input is 4:
        # STRETCH - UPDATE existing order

        PRINT orders list with its index values
        GET user input for order index value

        FOR EACH key-value pair in selected order:
            GET user input for updated property
            IF user input is blank:
                do not update this property
            ELSE:
                update the property value with user input

    ELSE IF user input is 5:
        # STRETCH GOAL - DELETE courier
                    
        PRINT orders list
        GET user input for order index value
        DELETE order at index in order list
```
