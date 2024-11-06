SET SEARCH_PATH TO public;

-- Inserindo dados na tabela Users
INSERT INTO Users (username, password_hash) VALUES
('Luke', 'hash_luke_123'), -- USER 1
('Darth', 'hash_darth_456'), -- USER 2
('Chewbacca', 'hash_chewbacca_789'), -- USER 3
('Leia', 'hash_leia_123'), -- USER 4
('Han', 'hash_han_456'), -- USER 5
('Yoda', 'hash_yoda_789'); -- ADMIN 6

-- Inserindo dados na tabela Roles
INSERT INTO Roles (role_name) VALUES
('user'), -- 1
('admin'), -- 2
('moderator'), -- 3
('seller'); -- 4

-- Inserindo dados na tabela User_Roles
INSERT INTO User_Roles (user_id, role_id) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 2);

-----------------------------------------------------------------------------------------

-- Inserindo dados na tabela Product
INSERT INTO Product (product_name, product_brand, product_price, product_description, product_stock) VALUES
('Coca-Cola 275ml', 'Coca-Cola', 3.50, 'Refrigerante de cola', 100), -- PROD 1
('Pepsi 275ml', 'Pepsi', 3.50, 'Refrigerante de cola', 80), -- PROD 2
('Fanta Laranja 275ml', 'Coca-Cola', 3.00, 'Refrigerante de laranja', 60), -- PROD 3
('Batata Lays 60g', 'Lays', 2.00, 'Chips de batata sabor original', 50), -- PROD 4
('Chocolate ao Leite 85g', 'Nestlé', 2.50, 'Delicioso chocolate ao leite', 30), -- PROD 5
('Kit-Kat 45g', 'Nestlé', 5.00, 'Biscoito waffle coberto de chocolate ao leite', 30), -- PROD 6
('Doritos 60g', 'Doritos', 8.50, 'Chips de milho sabor queijo', 50), -- PROD 7
('Agua Mineral 297ml', 'Indaia', 2.75, 'Agua mineral', 40), -- PROD 8
('Suco de Laranja 275ml', 'Del Valle', 4.00, 'Suco de laranja', 50), -- PROD 9
('Suco de Uva 275ml', 'Del Valle', 4.00, 'Suco de uva', 50), -- PROD 10
('Sanduiche 195g', 'Sadwich', 7.00, 'Sanduiche de presunto e queijo', 10); -- PROD 11

-- Inserindo dados na tabela VendingMachine
INSERT INTO VendingMachine (location, status) VALUES
('8 andar', 'online'), -- VM 1
('4 andar', 'online'), -- VM 2
('9 andar', 'offline'), -- VM 3
('terreo', 'online'); -- VM 4

-- Inserindo dados na tabela VM_Products
INSERT INTO VM_Products (vending_machine_id, product_id, vm_product_stock) VALUES
-- Coca-Cola 275ml
(1, 1, 50),
(2, 1, 25),
(4, 1, 25), --
-- Pepsi 275ml
(1, 2, 40),
(2, 2, 20),
(4, 2, 20), --
-- Fanta Laranja 275ml
(1, 3, 30),
(2, 3, 15),
(4, 3, 15), --
-- Batata Lays 60g
(1, 4, 20),
(2, 4, 10),
(4, 4, 10), --
-- Chocolate ao Leite 85g
(1, 5, 8),
(2, 5, 7),
(4, 5, 15), --
-- Kit-Kat 45g
(1, 6, 5),
(2, 6, 5),
(4, 6, 20), --
-- Doritos 60g
(1, 7, 15),
(2, 7, 15),
(4, 7, 20), --
-- Agua Mineral 297ml
(1, 8, 10),
(2, 8, 10),
(4, 8, 20), --
-- Suco de Laranja 275ml
(1, 9, 10),
(2, 9, 10),
(4, 9, 30), --
-- Suco de Uva 275ml
(1, 10, 15),
(2, 10, 20),
(4, 10, 15), --
-- Sanduiche 195g
(1, 11, 3),
(2, 11, 5),
(4, 11, 2); --

-----------------------------------------------------------------------------------------

-- Inserindo dados na tabela Purchase
INSERT INTO Purchase (purchase_date, purchase_price, vending_machine_id, user_id) VALUES
(NOW(), 10.00, 1, 1), --1
(NOW(), 2.00, 2, 2), --2
(NOW(), 3.50, 1, 3), --3
(NOW(), 7.50, 1, 1), -- 4
(NOW(), 12.00, 4, 5), -- 5
(NOW(), 14.00, 4, 4); -- 6

-- Inserindo dados na tabela Purchase_Items
INSERT INTO Purchase_Items (purchase_id, product_id, quantity, item_price) VALUES
--COMPRA 1
(1, 1, 2, 3.50),
(1, 3, 1, 3.00),
--COMPRA 2
(2, 4, 1, 2.00),
--COMPRA 3
(3, 1, 1, 3.50),
--COMPRA 4
(4, 5, 3, 2.50),
--COMPRA 5
(5, 4, 2, 2.00),
(5, 5, 1, 2.50),
(5, 8, 2, 2.75),
--COMPRA 6
(6, 11, 2, 7.00);

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