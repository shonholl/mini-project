CREATE TABLE orders (
order_id INT NOT NULL AUTO_INCREMENT,
customer_name VARCHAR(255) NOT NULL,
customer_address VARCHAR(255) NOT NULL,
customer_phone VARCHAR(255) NOT NULL,
courier_id INT NOT NULL,
status VARCHAR(255) NOT NULL,
product_id INT NOT NULL,
PRIMARY KEY(order_id),
FOREIGN KEY (courier_id) REFERENCES couriers(courier_id),
FOREIGN KEY (product_id) REFERENCES products(product_id)
);