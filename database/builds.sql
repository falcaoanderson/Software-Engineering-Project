DROP SCHEMA IF EXISTS public cascade;
CREATE SCHEMA public;
SET SEARCH_PATH TO public;

CREATE TABLE Product
(
  product_id SERIAL PRIMARY KEY,
  product_name VARCHAR(50) NOT NULL,
  product_brand VARCHAR(50) NOT NULL,
  product_price DECIMAL(10, 2) NOT NULL,
  product_description TEXT NOT NULL,
  product_stock INT NOT NULL
);

CREATE TABLE VendingMachine
(
  vending_machine_id SERIAL PRIMARY KEY,
  location VARCHAR(100) NOT NULL,
  status VARCHAR(10) NOT NULL
);

CREATE TABLE Users
(
  user_id SERIAL PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE Review
(
  review_id SERIAL PRIMARY KEY,
  comment TEXT NOT NULL,
  rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  user_id INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Purchase
(
  purchase_id SERIAL PRIMARY KEY,
  purchase_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  purchase_price DECIMAL(10, 2) NOT NULL,
  vending_machine_id INT NOT NULL,
  user_id INT NOT NULL,
  FOREIGN KEY (vending_machine_id) REFERENCES VendingMachine(vending_machine_id),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE VM_Products
(
  vending_machine_id INT NOT NULL,
  product_id INT NOT NULL,
  vm_product_stock INT NOT NULL,
  PRIMARY KEY (vending_machine_id, product_id),
  FOREIGN KEY (vending_machine_id) REFERENCES VendingMachine(vending_machine_id),
  FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

CREATE TABLE Purchase_Items
(
  purchase_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  item_price DECIMAL(10, 2) NOT NULL, -- Preço do produto no momento da compra
  PRIMARY KEY (purchase_id, product_id),
  FOREIGN KEY (purchase_id) REFERENCES Purchase(purchase_id),
  FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

CREATE TABLE Product_Review
(
  product_id INT NOT NULL,
  review_id INT NOT NULL,
  PRIMARY KEY (product_id, review_id),
  FOREIGN KEY (product_id) REFERENCES Product(product_id),
  FOREIGN KEY (review_id) REFERENCES Review(review_id)
);

CREATE TABLE VM_Review
(
  vending_machine_id INT NOT NULL,
  review_id INT NOT NULL,
  PRIMARY KEY (vending_machine_id, review_id),
  FOREIGN KEY (vending_machine_id) REFERENCES VendingMachine(vending_machine_id),
  FOREIGN KEY (review_id) REFERENCES Review(review_id)
);
