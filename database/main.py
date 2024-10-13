from conn import connect, shutdown

def main():
    connection = connect()

    # Criar um cursor
    cursor = connection.cursor()

    # Executar uma query
    # cursor.execute("SELECT * FROM public.users") 
    cursor.execute("""
        SELECT 
            p.product_name,
            SUM(vmp.vm_product_stock) AS total_stock
        FROM 
            vendingmachine vm
        JOIN 
            vm_products vmp ON vm.vending_machine_id = vmp.vending_machine_id
        JOIN 
            product p ON vmp.product_id = p.product_id
        GROUP BY 
            p.product_id
        ORDER BY 
            p.product_id;
    """)

    # Recuperar os resultados
    users = cursor.fetchall()
    for user in users:
        print(user)

    shutdown(connection, cursor)

if __name__ == "__main__":
    main()