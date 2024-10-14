def get_vm_list(cursor):
    query = """
    SELECT 
        vm.vending_machine_id,
        vm.location,
        vm.status,
        ROUND(avg(r.rating), 2) as average_rating
    FROM 
        vendingmachine vm
    LEFT JOIN
        vm_review vmr ON vmr.vending_machine_id = vm.vending_machine_id
    LEFT JOIN
        review r ON vmr.review_id = r.review_id
    GROUP BY
        vm.vending_machine_id
    ORDER BY
        vending_machine_id;
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()

    return rows

def get_products_from_vm(cursor, vm_id):
    query = """
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
    vmp.vending_machine_id = %s AND vmp.vm_product_stock > 0;
    """

    cursor.execute(query, (vm_id,))
    rows = cursor.fetchall()

    return rows

def get_avg_rating(cursor, vm_id):
    query = """
    SELECT
        ROUND(avg(r.rating), 2) as average_rating
    FROM 
        vm_review as vmr
    JOIN
        review r ON vmr.review_id = r.review_id
    WHERE
        vmr.vending_machine_id = %s;
    """

    cursor.execute(query, (vm_id,))
    avg = cursor.fetchall()

    return avg[0][0]

def get_reviews_from_vm(cursor, vm_id):
    query = """
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
        vmr.vending_machine_id = %s;
    """

    cursor.execute(query, (vm_id,))
    rows = cursor.fetchall()

    return rows