from conn import connect

#Função para obter o perfil de uma vending machine
def get_vending_machine_profile(vending_machine_id):
    try:
        connection = connect()
        cursor = connection.cursor()
        
        # Query para as vending machines
        query = """
        SELECT vm.location AS vending_machine_location, p.product_name AS product_name, 
        p.product_price AS product_price,
        r.rating AS machine_rating,
        r.comment AS machine_comment
        FROM 
        VendingMachine vm
        LEFT JOIN 
        VM_Products vmp ON vm.vending_machine_id = vmp.vending_machine_id
        LEFT JOIN 
        Product p ON vmp.product_id = p.product_id
        LEFT JOIN 
        VM_Review vmr ON vm.vending_machine_id = vmr.vending_machine_id
        LEFT JOIN 
        Review r ON vmr.review_id = r.review_id
        WHERE 
        vm.vending_machine_id = %s;
        """
        cursor.execute(query, (vending_machine_id,))
        results = cursor.fetchall()
        
        if results:
            print(f"Perfil da Vending Machine ID: {vending_machine_id}\n")
            for row in results:
                localizacao, produto, preco, avaliacao, comentario = row
                print(f"Localização: {localizacao}")
                print(f"Produto: {produto}, Preço: R${preco:.2f}")
                print(f"Avaliação: {avaliacao}, Comentário: {comentario}\n")
        else:
            print("Nenhum dado encontrado para a vending machine.")
    
    except Exception as error:
        print("Erro ao buscar o perfil da vending machine:", error)
    finally:
        if connection:
            cursor.close()
            connection.close()