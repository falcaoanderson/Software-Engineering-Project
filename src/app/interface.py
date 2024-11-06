from src.app.printdata import PrintData
from src.utils.console_utils import clean_screen
from src.database.productdata import ProductData
from src.database.vmdata import VendingMachineData
from src.database.conn import DatabaseConnection
import streamlit as st
import os

class Interface(ProductData, VendingMachineData, DatabaseConnection):
    def __init__(self, print_data):
        self.print_data = print_data

    def searchMenu(self):
        """
        Displays a menu for searching and viewing details of vending machines.
        The method runs in a loop, allowing the user to search for vending machines
        and view their details. The user can choose to search again or exit the menu.
        Workflow:
        1. Display a list of vending machines.
        2. Prompt the user to enter a vending machine ID to view its details.
        3. If the user enters -1, exit the menu.
        4. If the user enters an invalid ID, prompt again.
        5. After viewing details, ask the user if they want to search again.
        User Inputs:
        - Vending Machine ID: Numeric ID of the vending machine to view details.
        - Search Again Option: 'y' to search again, 'n' to exit.
        Raises:
        - ValueError: If the user enters a non-numeric vending machine ID.
        """
        
        running = True
        it = 0

        while running:
            if it > 0:
                # Pergunta se o usuário quer realizar uma nova busca
                op = st.selectbox("Deseja realizar uma nova busca?", ["Sim", "Não"])
                
                if op == "Não":
                    running = False
                    break

            if not running:
                break
            
            # Limpar a tela (não é necessário no Streamlit, o layout vai sendo atualizado)
            
            # Obter a lista de máquinas de vendas
            db = VendingMachineData("vmdb", os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), "localhost", "5432")
            db.connect()
            vm_list = db.get_vm_list()
            vm_ids = [vm[0] for vm in vm_list]
            
            # Exibir a lista de máquinas de vendas como tabela no Streamlit
            st.write("Máquinas de Vendas Disponíveis:")
            st.table(vm_list)

            # Segundo loop para garantir que o ID da máquina de vendas seja válido
            while True:
                # Solicitar ao usuário para escolher a ID de uma máquina de vendas
                vm_id_input = st.text_input("Digite o ID da Máquina de Vendas para ver detalhes: [-1 para voltar]")
                
                if vm_id_input:
                    try:
                        vm_id = int(vm_id_input)
                        
                        if vm_id == -1:
                            running = False
                            break
                        elif vm_id in vm_ids:
                            # Exibir detalhes da máquina de vendas selecionada
                            st.write(f"Detalhes da Máquina {vm_id}:")
                            self.print_data.display_vm_details(vm_id)
                            break  # Sai do segundo loop após exibir os detalhes
                        else:
                            st.warning("ID da máquina inválido, tente novamente.")

                    except ValueError:
                        st.warning("ID inválido, por favor, insira um número válido.")

            it += 1
    
    def stockMenu(self):
        """
        Displays the stock menu and allows the user to search for product details.
        The method runs in a loop, prompting the user to enter a product ID to view its details.
        After each search, the user is asked if they want to search again. The loop continues
        until the user chooses to exit.
        Workflow:
        1. Display all products in stock.
        2. Prompt the user to enter a product ID to view details.
        3. If the user enters -1, exit the menu.
        4. If the user enters a valid product ID, display the product details.
        5. Ask the user if they want to search again. If 'n', exit the menu; if 'y', continue.
        Note:
        - The screen is cleared before displaying the stock.
        - Input is validated to ensure a numeric product ID is entered.
        Raises:
            ValueError: If the input product ID is not a valid integer.
        """

        running = True
        it = 0

        while running:
            if it > 0:
                while True:
                    op = input("Do you want to search again? [y/n]: ").strip().lower()

                    if op == "n":
                        running = False
                        break
                    elif op == "y":
                        break
                    else:
                        print("Invalid option, please enter 'y' for yes or 'n' for no.")
            
            if not running:
                break
            
            clean_screen()

            self.print_data.display_all_products_stock()

            while True:
                product_id_input = input("Enter Product ID to view details: [-1 to go back]: ").strip()

                try:
                    product_id = int(product_id_input)

                    if product_id == -1:
                        running = False
                        break
                    else:
                        print("")
                        self.print_data.display_product_stock(product_id)
                        break
                except ValueError:
                    print("Invalid ID, please enter a valid numeric ID.")

            it += 1


if __name__ == "__main__":
    print("Running Interface")

    import os
    from dotenv import load_dotenv
    load_dotenv()

    print_data = PrintData("vmdb", os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), "localhost", "5432")
    print_data.connect()

    interface = Interface(print_data)
    # interface.searchMenu()
    interface.stockMenu()

    print_data.shutdown()
