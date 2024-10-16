from src.database.conn import DatabaseConnection

class VendingMachineData(DatabaseConnection):
    """
    A subclass of DatabaseConnection to handle Vending Machine related queries.
    """
    def get_vm_list(self):
        """
        Retrieves a list of vending machines along with their information and average user ratings.

        Returns:
        - A list of tuples containing:
            - vending_machine_id (int): The ID of the vending machine.
            - location (str): The location of the vending machine.
            - status (str): The current status of the vending machine.
            - average_rating (float): The average user rating.
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
        self.execute_query(query)
        return self.fetch_results()

    def get_products_from_vm(self, vm_id):
        """
        Retrieves a list of products available in a specific vending machine.

        Parameters:
        - vm_id (int): The ID of the vending machine.

        Returns:
        - A list of tuples containing:
            - product_id (int): The ID of the product.
            - product_name (str): The name of the product.
            - product_brand (str): The brand of the product.
            - product_price (float): The price of the product.
            - product_description (str): The description of the product.
            - product_stock (int): The available stock in the vending machine.
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
        self.execute_query(query, (vm_id,))
        return self.fetch_results()

    def get_avg_rating(self, vm_id):
        """
        Calculates the average rating for a specific vending machine.

        Parameters:
        - vm_id (int): The ID of the vending machine.

        Returns:
        - average_rating (float): The average rating, rounded to two decimal places.
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
        self.execute_query(query, (vm_id,))
        result = self.fetch_results()
        return result[0][0] if result else None

    def get_reviews_from_vm(self, vm_id):
        """
        Retrieves a list of reviews for a specific vending machine.

        Parameters:
        - vm_id (int): The ID of the vending machine.

        Returns:
        - A list of tuples containing:
            - review_id (int): The ID of the review.
            - rating (float): The user's rating.
            - comment (str): The user's comment.
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
        self.execute_query(query, (vm_id,))
        return self.fetch_results()
    
# Example usage
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()

    # Initialize the VendingMachineData class with database connection details
    db = VendingMachineData("vmdb", os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), "localhost", "5432")    
    # Connect to the database
    db.connect()

    print("")

    vms = db.get_vm_list()
    for vm in vms:
        print(vm)

    print("")

    products = db.get_products_from_vm(2)
    for product in products:
        print(product)

    print("")

    avg_rating = db.get_avg_rating(2)
    print(avg_rating)

    print("")

    reviews = db.get_reviews_from_vm(2)
    for review in reviews:
        print(review)

    print("")

    # Shutdown the database connection
    db.shutdown()