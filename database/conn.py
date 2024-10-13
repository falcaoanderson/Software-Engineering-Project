import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
db_password = os.getenv("DB_PASSWORD")

def connect():
    try:
        # Conectar ao banco de dados
        connection = psycopg2.connect(
            dbname="vmdb",
            user="postgres",
            password=db_password,
            host="localhost",
            port="5432"
        )
        print("Conexão estabelecida com sucesso.")

        return connection

    except Exception as e:
        print("Erro ao conectar ao banco de dados:\n", e)

def shutdown(connection, cursor):
    # Fechar o cursor e a conexão
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
    print("Conexão encerrada.")