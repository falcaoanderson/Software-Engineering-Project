def get_product_list(cursor):
    """
    Retrieves a list of products from the database.
    Args:
        cursor: The database cursor used to execute the query.
    Returns:
        list of tuple: A list of tuples where each tuple contains the following fields:
            - id (int): The product ID.
            - name (str): The product name.
            - brand (str): The product brand.
            - price (float): The product price.
            - product_description (str): The product description.
            - stock (int): The product stock quantity.
    """

    query = """
    SELECT 
        p.product_id as id,
        p.product_name as name,
        p.product_brand as brand,
        p.product_price as price,
        p.product_description as product_description,
        p.product_stock as stock
    FROM
        product p;
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()

    return rows

def get_product_stock(cursor, product_id):
    """
    Retrieves the stock information of a specific product across all vending machines.
    Args:
        cursor (Cursor): A database cursor object used to execute SQL queries.
        product_id (int): The ID of the product for which stock information is to be retrieved.
    Returns:
        list: A list of dictionaries, each containing the following keys:
            - vm_id (int): The ID of the vending machine.
            - location (str): The location of the vending machine.
            - status (str): The status of the vending machine.
            - stock (int): The stock level of the product in the vending machine.
    """

    query = """
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
        vmp.product_id = %s;
    """
    
    cursor.execute(query, (product_id,))
    rows = cursor.fetchall()

    return rows

# from conn import connect

# connection = connect()
# cursor = connection.cursor()

# rows = get_product_list(cursor)
# for row in rows:
#     print(row)

# print("\n")

# rows = get_product_stock(cursor, 7)
# for row in rows:
#     print(row)