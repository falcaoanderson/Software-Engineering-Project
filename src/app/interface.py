from src.app.printdata import PrintData
from src.utils.console_utils import clean_screen

class Interface:
    def __init__(self, print_data):
        self.print_data = print_data

    def searchMenu(self):
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

            self.print_data.display_vm_list()

            while True:
                vm_id_input = input("Enter Vending Machine ID to view details: [-1 to go back]: ").strip()

                try:
                    vm_id = int(vm_id_input)

                    if vm_id == -1:
                        break
                    else:
                        print("")
                        self.print_data.display_vm_details(vm_id)
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
    interface.searchMenu()

    print_data.shutdown()
