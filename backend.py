import sqlite3
from datetime import datetime

# Função para inicializar o banco de dados e criar as tabelas
def inicializar_banco():
    conexao = sqlite3.connect("vending_machine.db")
    cursor = conexao.cursor()

    # Criação da tabela de problemas
    cursor.execute('''CREATE TABLE IF NOT EXISTS Problemas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario TEXT,
                        tipo TEXT,
                        descricao TEXT,
                        data_reportada TEXT,
                        status TEXT DEFAULT "Aberto"
                    )''')
    conexao.commit()
    conexao.close()

# Função para adicionar um problema ao banco de dados
def adicionar_problema(usuario, tipo, descricao):
    conexao = sqlite3.connect("vending_machine.db")
    cursor = conexao.cursor()

    data_reportada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO Problemas (usuario, tipo, descricao, data_reportada) VALUES (?, ?, ?, ?)",
                   (usuario, tipo, descricao, data_reportada))
    conexao.commit()
    conexao.close()

# Função para obter problemas do banco de dados
def obter_problemas():
    conexao = sqlite3.connect("vending_machine.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM Problemas WHERE status = 'Aberto'")
    problemas = cursor.fetchall()
    conexao.close()
    return problemas
