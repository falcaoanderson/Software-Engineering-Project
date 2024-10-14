def get_vm_list(cursor):
    """
    Retrieves a list of vending machines along with their information and average user ratings.

    Parameters:
    - cursor: The cursor object used to execute the SQL query.

    Returns:
    - A list of tuples, where each tuple contains:
        - vending_machine_id (int): The ID of the vending machine.
        - location (str): The location of the vending machine.
        - status (str): The current status of the vending machine (e.g., operational, out of service).
        - average_rating (float): The average user rating for the vending machine (rounded to two decimal places).
    """

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
    """
    Retrieves a list of products available in a specific vending machine.

    Parameters:
    - cursor: The cursor object used to execute the SQL query.
    - vm_id (int): The ID of the vending machine from which to fetch the products.

    Returns:
    - A list of tuples, where each tuple contains:
        - product_id (int): The ID of the product.
        - product_name (str): The name of the product.
        - product_brand (str): The brand of the product.
        - product_price (float): The price of the product.
        - product_description (str): The description of the product.
        - product_stock (int): The available stock of the product in the vending machine.
    """

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
    """
    Calculates the average rating for a specific vending machine.

    Parameters:
    - cursor: The cursor object used to execute the SQL query.
    - vm_id (int): The ID of the vending machine for which the average rating will be calculated.

    Returns:
    - average_rating (float): The average rating for the vending machine (rounded to two decimal places).
    """

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
    """
    Retrieves a list of reviews for a specific vending machine.

    Parameters:
    - cursor: The cursor object used to execute the SQL query.
    - vm_id (int): The ID of the vending machine for which to fetch the reviews.

    Returns:
    - A list of tuples, where each tuple contains:
        - review_id (int): The ID of the review.
        - rating (float): The rating given by the user.
        - comment (str): The user's comment about the vending machine.
        - username (str): The username of the review's author.
    """

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