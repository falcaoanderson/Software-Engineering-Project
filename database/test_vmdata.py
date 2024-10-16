import unittest
from unittest.mock import patch
from vmdata import VendingMachineData

class TestVendingMachineData(unittest.TestCase):

    @patch.object(VendingMachineData, 'fetch_results')
    @patch.object(VendingMachineData, 'execute_query')
    def test_get_vm_list_success(self, mock_execute_query, mock_fetch_results):
        # Dados simulados que serão retornados pelo fetch_results
        mock_fetch_results.return_value = [
            (1, 'Location A', 'Active', 4.5),
            (2, 'Location B', 'Inactive', 3.8)
        ]

        # Criando a instância de VendingMachineData e chamando o método get_vm_list
        db = VendingMachineData('test_db', 'user', 'password', 'localhost', '5432')
        vm_list = db.get_vm_list()

        # Verificando se a query foi executada corretamente
        mock_execute_query.assert_called_once_with("""
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
        """)
        # Verificando se os resultados retornados são os esperados
        self.assertEqual(vm_list, [
            (1, 'Location A', 'Active', 4.5),
            (2, 'Location B', 'Inactive', 3.8)
        ])

    @patch.object(VendingMachineData, 'fetch_results')
    @patch.object(VendingMachineData, 'execute_query')
    def test_get_products_from_vm_success(self, mock_execute_query, mock_fetch_results):
        # Dados simulados que serão retornados pelo fetch_results
        mock_fetch_results.return_value = [
            (1, 'Product A', 'Brand A', 10.99, 'Description A', 100),
            (2, 'Product B', 'Brand B', 20.99, 'Description B', 50)
        ]

        # Criando a instância de VendingMachineData e chamando o método get_products_from_vm
        db = VendingMachineData('test_db', 'user', 'password', 'localhost', '5432')
        products = db.get_products_from_vm(1)

        # Verificando se a query foi executada corretamente
        mock_execute_query.assert_called_once_with("""
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
        """, (1,))
        # Verificando se os resultados retornados são os esperados
        self.assertEqual(products, [
            (1, 'Product A', 'Brand A', 10.99, 'Description A', 100),
            (2, 'Product B', 'Brand B', 20.99, 'Description B', 50)
        ])

    @patch.object(VendingMachineData, 'fetch_results')
    @patch.object(VendingMachineData, 'execute_query')
    def test_get_avg_rating_success(self, mock_execute_query, mock_fetch_results):
        # Dados simulados que serão retornados pelo fetch_results
        mock_fetch_results.return_value = [(4.25,)]

        # Criando a instância de VendingMachineData e chamando o método get_avg_rating
        db = VendingMachineData('test_db', 'user', 'password', 'localhost', '5432')
        avg_rating = db.get_avg_rating(1)

        # Verificando se a query foi executada corretamente
        mock_execute_query.assert_called_once_with("""
        SELECT
            ROUND(avg(r.rating), 2) as average_rating
        FROM 
            vm_review as vmr
        JOIN
            review r ON vmr.review_id = r.review_id
        WHERE
            vmr.vending_machine_id = %s;
        """, (1,))
        # Verificando se o resultado retornado é o esperado
        self.assertEqual(avg_rating, 4.25)

    @patch.object(VendingMachineData, 'fetch_results')
    @patch.object(VendingMachineData, 'execute_query')
    def test_get_reviews_from_vm_success(self, mock_execute_query, mock_fetch_results):
        # Dados simulados que serão retornados pelo fetch_results
        mock_fetch_results.return_value = [
            (1, 5.0, 'Bom', 'Yoda'),
            (2, 4.0, 'Pode melhorar', 'R2D2')
        ]

        # Criando a instância de VendingMachineData e chamando o método get_reviews_from_vm
        db = VendingMachineData('test_db', 'user', 'password', 'localhost', '5432')
        reviews = db.get_reviews_from_vm(1)

        # Verificando se a query foi executada corretamente
        mock_execute_query.assert_called_once_with("""
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
        """, (1,))
        # Verificando se os resultados retornados são os esperados
        self.assertEqual(reviews, [
            (1, 5.0, 'Bom', 'Yoda'),
            (2, 4.0, 'Pode melhorar', 'R2D2')
        ])

if __name__ == '__main__':
    unittest.main()
