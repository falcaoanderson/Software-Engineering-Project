SET SEARCH_PATH TO public;

-- Inserindo dados na tabela Users
INSERT INTO Users (username, password_hash) VALUES
('alice', 'hash_alice123'),
('bob', 'hash_bob456'),
('charlie', 'hash_charlie789');

-----------------------------------------------------------------------------------------

-- Inserindo dados na tabela Product
INSERT INTO Product (product_name, product_brand, product_price, product_description, product_stock) VALUES
('Coca-Cola', 'Coca-Cola', 3.50, 'Refrigerante de cola', 100),
('Pepsi', 'Pepsi', 3.50, 'Refrigerante de cola', 80),
('Fanta Laranja', 'Coca-Cola', 3.00, 'Refrigerante de laranja', 60),
('Chips de Batata', 'Lays', 2.00, 'Chips de batata sabor original', 50),
('Chocolate ao Leite', 'Nestlé', 2.50, 'Delicioso chocolate ao leite', 30);

-- Inserindo dados na tabela VendingMachine
INSERT INTO VendingMachine (location, status) VALUES
('8 andar', 'online'),
('4 andar', 'online'),
('9 andar', 'offline');

-- Inserindo dados na tabela VM_Products
INSERT INTO VM_Products (vending_machine_id, product_id, vm_product_stock) VALUES
(1, 1, 100),
(1, 2, 80),
(1, 3, 60),
(2, 4, 50),
(2, 5, 30);

-----------------------------------------------------------------------------------------

-- Inserindo dados na tabela Purchase
INSERT INTO Purchase (purchase_date, purchase_price, vending_machine_id, user_id) VALUES
(NOW(), 10.00, 1, 1),
(NOW(), 2.00, 2, 2),
(NOW(), 3.50, 1, 3),
(NOW(), 7.50, 1, 1);

-- Inserindo dados na tabela Purchase_Items
INSERT INTO Purchase_Items (purchase_id, product_id, quantity, item_price) VALUES
(1, 1, 2, 3.50),
(1, 3, 1, 3.00),
(2, 4, 1, 2.00),
(3, 1, 1, 3.50),
(4, 5, 3, 2.50);

-----------------------------------------------------------------------------------------

-- Inserindo dados na tabela Review
INSERT INTO Review (comment, rating, user_id) VALUES
('Ótima máquina, muito rápida!', 5, 1),
('Boa variedade!', 4, 2),
('A máquina estava fora de serviço.', 2, 3),
('Adoro a Fanta, sempre pego!', 5, 1),
('Muito caro!', 3, 2);

-- Inserindo dados na tabela Product_Review
INSERT INTO Product_Review (product_id, review_id) VALUES
(4, 4),
(5, 5);

-- Inserindo dados na tabela VM_Review
INSERT INTO VM_Review (vending_machine_id, review_id) VALUES
(1, 1),
(2, 2),
(3, 3);