import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host,
    user,
    password,
    database
)


cursor = connection.cursor()

# Execute SQL query
cursor.execute('SELECT product_id, product_name, product_price FROM products')

# Gets all rows from the result
rows = cursor.fetchall()
for row in rows:
    print(f'product id: {int(row[0])}, product name: {row[1]}, product price: {float(row[2])}')

#insert product and price into product table
user_product_name= input("Please enter a product name: ")
user_product_price = float(input("Please enter a product price: "))
sql = "INSERT INTO product(product_name, product_price) VALUES (%s,%s)"
val = (user_product_name,user_product_price)
cursor.execute(sql,val)
connection.commit()
print(cursor.rowcount,"record inserted.")

# Closes the cursor so will be unusable from this point 
cursor.close()

# Closes the connection to the DB
connection.close()