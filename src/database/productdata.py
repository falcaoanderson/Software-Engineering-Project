from src.database.conn import DatabaseConnection

class ProductData(DatabaseConnection):
    """
    A subclass of DatabaseConnection to handle product-related queries.
    """

    def get_product_list(self):
        """
        Retrieves a list of products from the database.
        
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
        try:
            if self.cursor is None:
                raise Exception("Connection is not established. Call the 'connect' method first.")

            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows

        except Exception as e:
            print("Error retrieving the product list:\n", e)
            return []

    def get_product_stock(self, product_id):
        """
        Retrieves the stock information of a specific product across all vending machines.

        Args:
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
        try:
            if self.cursor is None:
                raise Exception("Connection is not established. Call the 'connect' method first.")

            self.cursor.execute(query, (product_id,))
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print("Error retrieving the product stock:\n", e)
            return []

# Example usage
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()

    # Initialize the ProductQueries class with database connection details
    db = ProductData("vmdb", os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), "localhost", "5432")    
    # Connect to the database
    db.connect()

    # Retrieve the product list
    products = db.get_product_list()
    for product in products:
        print(product)

    print("\n")

    # Retrieve the stock information for a specific product
    product_id = 7  # Example product ID
    stock_info = db.get_product_stock(product_id)
    for stock in stock_info:
        print(stock)

    # Shutdown the database connection
    db.shutdown()