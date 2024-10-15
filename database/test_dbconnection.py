import unittest
from unittest.mock import patch, MagicMock
from conn import DatabaseConnection

class TestDatabaseConnection(unittest.TestCase):
    
    @patch('psycopg2.connect')
    def test_connect_success(self, mock_connect):
        # Mockando o objeto de conexão e cursor
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Criando a instância da classe
        db = DatabaseConnection('test_db', 'user', 'password', 'localhost', '5432')
        db.connect()

        # Verificando se o método connect do psycopg2 foi chamado com os parâmetros corretos
        mock_connect.assert_called_once_with(
            dbname='test_db', user='user', password='password', host='localhost', port='5432'
        )
        # Verificando se o cursor foi criado
        mock_connection.cursor.assert_called_once()
        self.assertEqual(db.cursor, mock_cursor)

if __name__ == '__main__':
    unittest.main()
