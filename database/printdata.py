from productdata import ProductData
from vmdata import VendingMachineData

class PrintData(ProductData, VendingMachineData):
    def display_vm_list(self):
        """
        Display a list of vending machines with their details.

        This method retrieves a list of vending machines and prints their ID, location, 
        status, and average rating in a formatted table. If the average rating is not 
        available, it displays 'N/A' instead.
        """
        vms = self.get_vm_list()

        print("List of Vending Machines:")
        print(f"{'ID':<5} {'Location':<20} {'Status':<10} {'Avg. Rating':<15}")
        print("-" * 50)

        for vm in vms:
            vm_id, location, status, avg_rating = vm
            if avg_rating is None:
                avg_rating = "N/A"
            print(f"{vm_id:<5} {location:<20} {status:<10} {avg_rating:<15}")

        print("\n")

    def display_products_from_vm(self, vm_id):
        """
        Display the list of products available in a specific vending machine.

        Parameters:
        - vm_id (int): The ID of the vending machine.

        This method retrieves the products available in the specified vending machine
        and prints their details in a formatted table.
        """
        products = self.get_products_from_vm(vm_id)

        print(f"Products available in Vending Machine {vm_id}:")
        print(f"{'ID':<5} {'Name':<25} {'Brand':<15} {'Description':<50} {'Price':<10} {'Stock':<5}")
        print("-" * 120)

        for product in products:
            product_id, name, brand, price, description, stock = product
            print(f"{product_id:<5} {name:<25} {brand:<15} {description:<50} R${price:<10.2f} {stock:<5}")

        print("\n")

    def display_avg_rating(self, vm_id):
        """
        Displays the average rating for a given vending machine.

        Parameters:
        - vm_id (int): The ID of the vending machine.

        This method retrieves and prints the average rating for the specified vending machine.
        """
        avg_rating = self.get_avg_rating(vm_id)
        print(f"Average Rating: {avg_rating}\n")

    def display_reviews_from_vm(self, vm_id):
        """
        Display reviews for a specific vending machine.

        Parameters:
        - vm_id (int): The ID of the vending machine.

        This method retrieves the reviews for the specified vending machine and
        prints their details in a formatted table.
        """
        reviews = self.get_reviews_from_vm(vm_id)

        print(f"Reviews for Vending Machine {vm_id}:")
        print(f"{'Review ID':<10} {'Rating':<7} {'Username':<15} {'Comment'}")
        print("-" * 60)

        for review in reviews:
            review_id, rating, comment, username = review
            print(f"{review_id:<10} {rating:<7} {username:<15} {comment}")

        print("\n")

    def display_vm_details(self, vm_id):
        """
        Display details for a specific vending machine.

        This method prints the details for a vending machine identified by `vm_id`.
        It includes the average rating, the list of products, and the reviews for 
        the vending machine.

        Parameters:
        - vm_id (int): The ID of the vending machine.
        """
        print(f"Details for Vending Machine {vm_id}:")
        self.display_avg_rating(vm_id)
        self.display_products_from_vm(vm_id)
        self.display_reviews_from_vm(vm_id)

    def display_all_products_stock(self):
        """
        Display the stock information for all products across all vending machines.

        This method retrieves the stock information for all products and prints it
        in a formatted table.
        """
        products = self.get_product_list()

        print("Stock Information for All Products:")
        print(f"{'ID':<5} {'Name':<25} {'Brand':<15} {'Price':<10} {'Description':<50} {'Stock':<5}")
        print("-" * 120)

        for product in products:
            product_id, name, brand, price, description, stock = product
            print(f"{product_id:<5} {name:<25} {brand:<15} R${price:<10.2f} {description:<50} {stock:<5}")

        print("\n")

    def display_product_stock(self, product_id):
        """
        Display the stock information for a specific product across all vending machines.

        Parameters:
        - product_id (int): The ID of the product.

        This method retrieves the stock information for the specified product and
        prints it in a formatted table.
        """
        stocks = self.get_product_stock(product_id)

        print(f"Stock Information for Product {product_id}:")
        print(f"{'VM ID':<5} {'Location':<15} {'Status':<10} {'Stock':<5}")
        print("-" * 40)

        for stock in stocks:
            vm_id, location, status, stock_level = stock
            print(f"{vm_id:<5} {location:<15} {status:<10} {stock_level:<5}")

        print("\n")

#Example of usage
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()

    print_data = PrintData("vmdb", os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), "localhost", "5432")
    print_data.connect()

    print_data.display_vm_list()
    print("")
    print_data.display_products_from_vm(1)
    print("")
    print_data.display_avg_rating(2)
    print("")
    print_data.display_reviews_from_vm(1)
    print("")
    print_data.display_vm_details(1)
    print("")
    print_data.display_all_products_stock()
    print("")
    print_data.display_product_stock(2)