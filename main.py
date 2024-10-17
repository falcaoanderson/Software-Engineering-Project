from src.app.printdata import PrintData
from src.app.interface import Interface
from src.utils.console_utils import clean_screen
import os 
from dotenv import load_dotenv

load_dotenv()

def main():
    print_data = PrintData("vmdb", os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), "localhost", "5432")
    print_data.connect()

    inteface = Interface(print_data)

    while True:
        clean_screen()
        while True:
            type_user = input("Enter '1' for User or '2' for Manager [or -1 to exit]: ").strip()

            if type_user in ["1", "2", "-1"]:
                break
            else:
                print("Invalid option, please enter '1' for User or '2' for Manager.")

        if type_user == "1":
            inteface.searchMenu()
        elif type_user == "2": 
            inteface.stockMenu()
        else:   
            break
    
    print_data.shutdown()

if __name__ == "__main__":
    main()