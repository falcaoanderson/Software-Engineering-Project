from src.app.printdata import PrintData
from src.app.interface import Interface
import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import psycopg2

load_dotenv()

def main():
    # Conectar ao banco de dados
    print_data = PrintData("vmdb", os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), "localhost", "5432")
    print_data.connect()

    interface = Interface(print_data)

    # Criar uma barra lateral com um título
    st.sidebar.title("Escolha o tipo de usuário")

    # Botões para escolha do tipo de usuário
    user_choice = st.button("Usuário")
    admin_choice = st.button("Admin")

    # Opção para sair
    if st.sidebar.button("Sair"):
        st.stop()

    # Exibir a escolha do usuário
    #st.header(f"Você escolheu: {user_choice}")

    if user_choice:
        # Chama o menu de pesquisa para usuário
        st.header(f"Usuário")
        interface.searchMenu()
        
    if admin_choice:
        # Chama o menu de estoque para gerente
        st.header(f"Admin")
        interface.stockMenu()

    else:
        st.warning("Escolha uma opção válida")

    # Fechar a conexão com o banco de dados ao final
    print_data.shutdown()

if __name__ == "__main__":
    main()
