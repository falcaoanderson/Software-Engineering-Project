from printdata import PrintData
import os 
from dotenv import load_dotenv

load_dotenv()

def main():
    print_data = PrintData("vmdb", os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), "localhost", "5432")
    print_data.connect()

    print_data.display_vm_list()

    vm_id = input("Enter Vending Machine ID to view details: ")
    print("\n")
    
    print_data.display_vm_details(vm_id)

    print_data.shutdown()

if __name__ == "__main__":
    main()