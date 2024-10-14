from conn import connect, shutdown
from queriesvis import vmsearch

def main():
    connection = connect()

    # Criar um cursor
    cursor = connection.cursor()
    
    vmsearch(cursor)
    
    shutdown(connection, cursor)

if __name__ == "__main__":
    main()