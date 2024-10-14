from queries14 import get_vm_list, get_avg_rating, get_reviews_from_vm, get_products_from_vm

def display_vm_list(cursor):
    """
    Display a list of vending machines with their details.
    Args:
        cursor: The database cursor to execute queries.
    The function retrieves a list of vending machines from the database using
    the `get_vm_list` function and prints their ID, location, status, and 
    average rating in a formatted table. If the average rating is not available,
    it displays 'N/A' instead.
    """
    vms = get_vm_list(cursor)
    
    print("List of Vending Machines:")
    print(f"{'ID':<5} {'Location':<20} {'Status':<10} {'Avg. Rating':<15}")
    print("-" * 50)
    
    for vm in vms:
        vm_id, location, status, avg_rating = vm
        if avg_rating is None:
            avg_rating = "N/A"
        print(f"{vm_id:<5} {location:<20} {status:<10} {avg_rating:<15}")
    
    print("\n")

def display_products_from_vm(cursor, vm_id):
    """
    Display the list of products available in a specific vending machine.
    Args:
        cursor: The database cursor to execute queries.
        vm_id (int): The ID of the vending machine.
    Returns:
        None: This function prints the products available in the specified vending machine.
    """
    products = get_products_from_vm(cursor, vm_id)
    
    print(f"Products available in Vending Machine {vm_id}:")
    print(f"{'ID':<5} {'Name':<25} {'Brand':<15} {'Description':<50} {'Price':<10} {'Stock':<5}")
    print("-" * 120)
    
    for product in products:
        product_id, name, brand, price, description, stock = product
        print(f"{product_id:<5} {name:<25} {brand:<15} {description:<50} R${price:<10.2f} {stock:<5}")
        # print(product)
    print("\n")

def display_avg_rating(cursor, vm_id):
    """
    Displays the average rating for a given VM.

    Args:
        cursor: The database cursor to execute the query.
        vm_id (int): The ID of the VM for which to display the average rating.

    Returns:
        None
    """
    avg_rating = get_avg_rating(cursor, vm_id)
    print(f"Average Rating: {avg_rating}\n")

def display_reviews_from_vm(cursor, vm_id):
    """
    Display reviews for a specific vending machine.
    Args:
        cursor: The database cursor to execute queries.
        vm_id (int): The ID of the vending machine whose reviews are to be displayed.
    Returns:
        None
    """
    reviews = get_reviews_from_vm(cursor, vm_id)
    
    print(f"Reviews for Vending Machine {vm_id}:")
    print(f"{'Review ID':<10} {'Rating':<7} {'Username':<15} {'Comment'}")
    print("-" * 60)
    
    for review in reviews:
        review_id, rating, comment, username = review
        print(f"{review_id:<10} {rating:<7} {username:<15} {comment}")
    
    print("\n")

def display_vm_details(cursor, vm_id):
    """
    Display details for a specific vending machine.

    This function prints the details for a vending machine identified by `vm_id`.
    It includes the average rating, the list of products, and the reviews for the vending machine.

    Args:
        cursor: The database cursor to execute queries.
        vm_id (int): The ID of the vending machine to display details for.

    Returns:
        None
    """
    print(f"Details for Vending Machine {vm_id}:")
    display_avg_rating(cursor, vm_id)
    display_products_from_vm(cursor, vm_id)
    display_reviews_from_vm(cursor, vm_id)

def vmsearch(cursor):
    """
    Searches for a vending machine and displays its details.
    This function first displays a list of vending machines using the provided database cursor.
    It then prompts the user to enter the ID of a vending machine to view its details and displays
    the details of the selected vending machine.
    Args:
        cursor: A database cursor object used to execute SQL queries.
    Returns:
        None
    """
    display_vm_list(cursor)
    
    vm_id = input("Enter Vending Machine ID to view details: ")
    print("\n")
    
    display_vm_details(cursor, vm_id)
