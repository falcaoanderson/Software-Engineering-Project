-- Lista todos os produtos:
SELECT 
  p.product_id as id,
  p.product_name as name,
  p.product_brand as brand,
  p.product_price as price,
  p.product_description as product_description,
  p.product_stock as stock
FROM
  product p;

-- Lista o estoque entre todas as vending manchine de um produto específico:
SELECT
  vm.vending_machine_id as vm_id,
  vm.location,
  vm.status,
  vmp.vm_product_stock as stock
FROM
  vm_products vmp
JOIN
  vendingmachine vm on vm.vending_machine_id = vmp.vending_machine_id
WHERE
  vmp.product_id = 1 /* id do produto */;

  