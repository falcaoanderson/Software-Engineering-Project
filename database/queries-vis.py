from queries import get_vm_list, get_avg_rating, get_reviews_from_vm, get_products_from_vm

def display_vm_list(cursor):
    vms = get_vm_list(cursor)
    
    print("List of Vending Machines:")
    print(f"{'ID':<5} {'Location':<20} {'Status':<10} {'Average Rating':<15}")
    print("-" * 50)
    
    for vm in vms:
        vm_id, location, status, avg_rating = vm
        print(f"{vm_id:<5} {location:<20} {status:<10} {avg_rating:<15}")
    
    print("\n")

def display_products_from_vm(cursor, vm_id):
    products = get_products_from_vm(cursor, vm_id)
    
    print(f"Products available in Vending Machine {vm_id}:")
    print(f"{'Product ID':<10} {'Name':<20} {'Brand':<15} {'Price':<10} {'Stock':<5}")
    print("-" * 60)
    
    for product in products:
        product_id, name, brand, price, stock = product
        print(f"{product_id:<10} {name:<20} {brand:<15} ${price:<10.2f} {stock:<5}")
    
    print("\n")

def display_avg_rating(cursor, vm_id):
    avg_rating = get_avg_rating(cursor, vm_id)
    print(f"Average Rating for Vending Machine {vm_id}: {avg_rating}\n")

def display_reviews_from_vm(cursor, vm_id):
    reviews = get_reviews_from_vm(cursor, vm_id)
    
    print(f"Reviews for Vending Machine {vm_id}:")
    print(f"{'Review ID':<10} {'Rating':<7} {'Username':<15} {'Comment'}")
    print("-" * 60)
    
    for review in reviews:
        review_id, rating, comment, username = review
        print(f"{review_id:<10} {rating:<7} {username:<15} {comment}")
    
    print("\n")

#Função para exibir as informações da vending machine
def display_vm_details(cursor, vm_id):
    print(f"Details for Vending Machine {vm_id}:")
    display_avg_rating(cursor, vm_id)
    display_products_from_vm(cursor, vm_id)
    display_reviews_from_vm(cursor, vm_id)

def main(cursor):
    display_vm_list(cursor)
    
    #Vamos pedir ao usuário para selecionar uma vending machine e exibir seus detalhes
    vm_id = input("Enter Vending Machine ID to view details: ")
    
    display_vm_details(cursor, vm_id)
