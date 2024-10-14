-- Lista todas as maquinas de venda:
SELECT 
    vm.vending_machine_id,
    vm.location,
    vm.status,
    avg(r.rating) as average_rating
FROM 
    vendingmachine vm
JOIN
    vm_review vmr ON vmr.vending_machine_id = vm.vending_machine_id
JOIN
    review r ON vmr.review_id = r.review_id
GROUP BY
    vm.vending_machine_id
ORDER BY
    vending_machine_id;


-- Lista todos os produtos de uma maquina de venda especificada:
SELECT 
  p.product_id,
  p.product_name,
  p.product_brand,
  p.product_price,
  p.product_description,
  vmp.vm_product_stock as product_stock
FROM
  vm_products vmp
JOIN
  product p ON vmp.product_id = p.product_id
WHERE 
  vmp.vending_machine_id = 1 /*troca 1 para o id do maquina*/ AND vmp.vm_product_stock > 0;


-- Calcula a media de avaliacao de uma maquina especificada:
SELECT
    avg(r.rating) as average_rating
FROM 
    vm_review as vmr
JOIN
    review r ON vmr.review_id = r.review_id
WHERE
    vmr.vending_machine_id = 1 /*troca 1 para o id do maquina*/;


-- Lista todos os reviews de uma maquina especificada:
SELECT
    vmr.review_id,
    r.rating,
    r.comment,
    u.username
FROM 
    vm_review as vmr
JOIN
    review r ON vmr.review_id = r.review_id
JOIN
    users u ON r.user_id = u.user_id
WHERE
    vmr.vending_machine_id = 1 /*troca 1 para o id do maquina*/;