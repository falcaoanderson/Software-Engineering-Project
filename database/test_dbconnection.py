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
   
    @patch('psycopg2.connect')
    def test_connect_failure(self, mock_connect):
        # Simulando uma falha na conexão
        mock_connect.side_effect = Exception("Connection failed")

        # Criando a instância da classe
        db = DatabaseConnection('test_db', 'user', 'password', 'localhost', '5432')
        db.connect()

        # Verificando se a conexão e o cursor permanecem como None após a falha
        self.assertIsNone(db.connection)
        self.assertIsNone(db.cursor)

    @patch('psycopg2.connect')
    def test_shutdown(self, mock_connect):
        # Mockando o objeto de conexão e cursor
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Criando a instância da classe e conectando
        db = DatabaseConnection('test_db', 'user', 'password', 'localhost', '5432')
        db.connect()
        db.shutdown()

        # Verificando se o cursor e a conexão foram fechados
        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()
    
    @patch('psycopg2.connect')
    def test_execute_query_success(self, mock_connect):
        # Mockando o objeto de conexão e cursor
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Criando a instância da classe e conectando
        db = DatabaseConnection('test_db', 'user', 'password', 'localhost', '5432')
        db.connect()
        db.execute_query("SELECT * FROM test_table")

        # Verificando se o método execute do cursor foi chamado com os parâmetros corretos
        mock_cursor.execute.assert_called_once_with("SELECT * FROM test_table", None)
        mock_connection.commit.assert_called_once()

    @patch('psycopg2.connect')
    def test_execute_query_without_connection(self, mock_connect):
        # Criando a instância da classe sem conectar
        db = DatabaseConnection('test_db', 'user', 'password', 'localhost', '5432')

        with self.assertRaises(Exception) as context:
            db.execute_query("SELECT * FROM test_table")

        # Verificando se a exceção foi levantada corretamente
        self.assertTrue("Connection is not established" in str(context.exception))
    
    @patch('psycopg2.connect')
    def test_fetch_results_success(self, mock_connect):
        # Mockando o objeto de conexão e cursor
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('row1',), ('row2',)]
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Criando a instância da classe e conectando
        db = DatabaseConnection('test_db', 'user', 'password', 'localhost', '5432')
        db.connect()
        results = db.fetch_results()

        # Verificando se o método fetchall do cursor foi chamado
        mock_cursor.fetchall.assert_called_once()
        # Verificando se os resultados retornados são os esperados
        self.assertEqual(results, [('row1',), ('row2',)])
    
    @patch('psycopg2.connect')
    def test_fetch_results_without_connection(self, mock_connect):
        # Criando a instância da classe sem conectar
        db = DatabaseConnection('test_db', 'user', 'password', 'localhost', '5432')
        with self.assertRaises(Exception) as context:
            db.fetch_results()

        # Verificando se a exceção foi levantada corretamente
        self.assertTrue("Connection is not established" in str(context.exception))

if __name__ == '__main__':
    unittest.main()
