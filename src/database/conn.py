import psycopg2

class DatabaseConnection:
    """
    A class to manage a PostgreSQL database connection and execute SQL operations.

    Attributes:
        db_name (str): The name of the database to connect to.
        db_user (str): The username used to authenticate.
        db_password (str): The password used to authenticate.
        db_host (str): The host where the database server is located.
        db_port (str): The port number used to connect to the database server.
        connection (psycopg2.extensions.connection): The connection object to the database.
        cursor (psycopg2.extensions.cursor): The cursor object used to execute SQL commands.
    """

    def __init__(self, db_name, db_user, db_password, db_host, db_port):
        """
        Initializes the DatabaseConnection class with the provided database parameters.

        Args:
            db_name (str): The name of the database.
            db_user (str): The username for the database.
            db_password (str): The password for the database.
            db_host (str): The host address of the database server.
            db_port (str): The port number of the database server.
        """
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.connection = None
        self.cursor = None

    def connect(self):
        """
        Establishes a connection to the PostgreSQL database.

        If the connection is successful, a cursor is created for executing SQL commands.
        If the connection fails, an exception is caught, and an error message is printed.
        """
        try:
            # Connect to the database
            self.connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port
            )
            self.cursor = self.connection.cursor()
            print("Connection to the database established successfully.")

        except Exception as e:
            print("Failed to connect to the database:\n", e)

    def shutdown(self):
        """
        Closes the database cursor and connection.

        Ensures that resources are properly released when the connection is no longer needed.
        """
        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None:
            self.connection.close()
        print("Database connection closed.")

    def execute_query(self, query, params=None):
        """
        Executes a SQL query on the connected database.

        Args:
            query (str): The SQL query to be executed.
            params (tuple, optional): A tuple of parameters to be used in the query.
        
        Raises:
            Exception: If the connection has not been established before executing the query.
        """
        try:
            if self.cursor is None:
                raise Exception("Connection is not established. Call the 'connect' method first.")

            self.cursor.execute(query, params)
            self.connection.commit()
            # print("SQL query executed successfully.")
        except Exception as e:
            print("Error executing the SQL query:\n", e)
            raise

    def fetch_results(self):
        """
        Retrieves the results of the last executed query.

        Returns:
            list: A list of tuples containing the rows returned by the query.
        
        Raises:
            Exception: If the connection has not been established before fetching results.
        """
        try:
            if self.cursor is None:
                raise Exception("Connection is not established. Call the 'connect' method first.")

            return self.cursor.fetchall()
        except Exception as e:
            print("Error fetching results from the database:\n", e) 
            raise

# Exemplo de uso
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    
    # Carregar variáveis de ambiente do arquivo .env
    load_dotenv()
    
    db = DatabaseConnection("vmdb", os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), "localhost", "5432")

    # Conectar ao banco de dados
    db.connect()

    # Executar uma consulta de exemplo (criação de tabela)
    create_table_query = """
    SELECT * FROM PRODUCT;
    """
    db.execute_query(create_table_query)
    rows = db.fetch_results()
    for row in rows:
        print(row)
    # Encerrar a conexão
    db.shutdown()