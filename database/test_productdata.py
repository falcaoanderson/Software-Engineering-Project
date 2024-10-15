import unittest
from unittest.mock import patch, MagicMock
from productdata import ProductData

class TestProductData(unittest.TestCase):

    @patch('psycopg2.connect')
    def test_get_product_list_success(self, mock_connect):
        # Mockando o objeto de conexão e cursor
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        
        # Dados simulados que serão retornados pelo fetchall
        mock_cursor.fetchall.return_value = [
            (1, 'Product A', 'Brand A', 10.99, 'Description A', 100),
            (2, 'Product B', 'Brand B', 20.99, 'Description B', 50)
        ]
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Criando a instância de ProductData e conectando
        db = ProductData('test_db', 'user', 'password', 'localhost', '5432')
        db.connect()
        product_list = db.get_product_list()

        # Verificando se a query foi executada corretamente
        mock_cursor.execute.assert_called_once_with("""
        SELECT 
            p.product_id as id,
            p.product_name as name,
            p.product_brand as brand,
            p.product_price as price,
            p.product_description as product_description,
            p.product_stock as stock
        FROM
            product p;
        """)

        # Verificando se os resultados retornados são os esperados
        self.assertEqual(product_list, [
            (1, 'Product A', 'Brand A', 10.99, 'Description A', 100),
            (2, 'Product B', 'Brand B', 20.99, 'Description B', 50)
        ])

if __name__ == "__main__":
    unittest.main()