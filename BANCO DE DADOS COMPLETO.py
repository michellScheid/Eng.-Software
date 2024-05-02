import mysql.connector

# Configurações de conexão ao banco de dados
host = "167.99.252.245"
user = "ESW2024_E4"
passwd = "123mudar"
database = "ESW2024_E4"

# Função para criar uma nova tabela
def criarTabela():
    try:
        connector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
        cursor = connector.cursor()

        tabela = input("Qual o nome da tabela que você quer criar? >>> ")
        cursor.execute(f"CREATE TABLE {tabela} (ID INT AUTO_INCREMENT PRIMARY KEY)")

        while True:
            add = input("Você deseja adicionar uma variável? (S/N) >>> ").upper()
            if add == "S":
                var_nome = input("Digite o nome da variável >>> ")
                var_tipo = input("Digite o tipo da variável >>> ")
                cursor.execute(f"ALTER TABLE {tabela} ADD {var_nome} {var_tipo}")
            elif add == "N":
                break
            else:
                print("Opção inválida.")

        print(f"Tabela {tabela} criada com sucesso!")
    except mysql.connector.Error as error:
        print("Erro ao criar tabela:", error)
    finally:
        cursor.close()
        connector.close()

# Função para atualizar dados em uma tabela
def atualizarDados(tabela):
    try:
        connector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
        cursor = connector.cursor()

        opcao = input(f"Deseja atualizar os dados na tabela {tabela}? (S/N): ").upper()
        if opcao == 'S':
            coluna = input(f"Qual coluna da tabela {tabela} você deseja atualizar? >>> ")
            valor_antigo = input(f"Qual o valor antigo na coluna {coluna} que você quer mudar? >>> ")
            novo_valor = input(f"Qual o novo valor para a coluna {coluna}? >>> ")

            sql = f"UPDATE {tabela} SET {coluna} = %s WHERE {coluna} = %s"
            cursor.execute(sql, (novo_valor, valor_antigo))
            connector.commit()

            if cursor.rowcount > 0:
                print("Registro(s) atualizado(s) com sucesso!")
            else:
                print(f"Nenhum registro encontrado com o valor antigo fornecido para a coluna {coluna}")
        elif opcao == 'N':
            print("Nenhum dado foi atualizado.")
        else:
            print("Opção inválida.")
    except mysql.connector.Error as error:
        print("Erro ao atualizar registro(s):", error)
        connector.rollback()
    finally:
        cursor.close()
        connector.close()

# Função para deletar dados de uma tabela
def deletarDados(tabela, atributo, valor):
    try:
        connector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
        cursor = connector.cursor()

        sql = f"DELETE FROM {tabela} WHERE {atributo} = %s"
        cursor.execute(sql, (valor,))
        connector.commit()

        if cursor.rowcount > 0:
            print("Registro(s) deletado(s) com sucesso!")
        else:
            print("Nenhum registro encontrado com o valor fornecido para o atributo:", atributo)
    except mysql.connector.Error as error:
        print("Erro ao deletar registro(s):", error)
        connector.rollback()
    finally:
        cursor.close()
        connector.close()

# Função para procurar dados em uma tabela
def procurarDados(tabela):
    try:
        connector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
        cursor = connector.cursor()

        opcao = input(f"Deseja procurar os dados na tabela {tabela}? (S/N): ").upper()
        if opcao == 'S':
            coluna_select = input(f"Qual a coluna da tabela {tabela} para selecionar? >>> ")
            cursor.execute(f"SELECT {coluna_select} FROM {tabela}")

            resultados = cursor.fetchall()
            if resultados:
                print("Resultados encontrados:")
                for resultado in resultados:
                    print(resultado)
            else:
                print("Nenhum resultado encontrado.")
        elif opcao == 'N':
            print("Nenhum dado foi procurado.")
        else:
            print("Opção inválida.")
    except mysql.connector.Error as error:
        print("Erro ao procurar dados:", error)
    finally:
        cursor.close()
        connector.close()

# Função para inserir dados em uma tabela específica
def inserirDados(tabela):
    try:
        connector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
        cursor = connector.cursor()

        if tabela.upper() == 'COMPRAS':
            nome = input("Qual o nome do produto? >>> ")
            codigo_de_barras = input("Qual o código de barras? >>> ")
            preco_de_compra = input("Qual o preço de compra? >>> ")
            estoque = input("Qual a quantidade de estoque? >>> ")
            quantidade_comprada = input("Qual a quantidade comprada? >>> ")
            marca = input("Qual a marca do produto? >>> ")
            categoria = input("Qual a categoria do produto? >>> ")

            sql = "INSERT INTO COMPRAS (NOME, CODIGO_DE_BARRA, PREÇO_DE_COMPRA, ESTOQUE, QUANTIDADE_COMPRADA, MARCA, CATEGORIA) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (nome, codigo_de_barras, preco_de_compra, estoque, quantidade_comprada, marca, categoria))

        elif tabela.upper() == 'ESTOQUE':
            nome = input("Qual o nome do produto? >>> ")
            codigo_de_barras = input("Qual o código de barras? >>> ")
            endereco_de_estoque = input("Qual o endereço de estoque? >>> ")
            estoque = input("Qual a quantidade de estoque? >>> ")
            quantidade_vendida = input("Qual a quantidade vendida? >>> ")
            marca = input("Qual a marca do produto? >>> ")
            categoria = input("Qual a categoria do produto? >>> ")

            sql = "INSERT INTO ESTOQUE (NOME, CODIGO_DE_BARRA, ENDEREÇO_DE_ESTOQUE, ESTOQUE, QUANTIDADE_VENDIDA, MARCA, CATEGORIA) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (nome, codigo_de_barras, endereco_de_estoque, estoque, quantidade_vendida, marca, categoria))

        elif tabela.upper() == 'PRODUTO':
            nome_do_produto = input("Qual o nome do produto? >>> ")
            codigo_de_barras = input("Qual o código de barras? >>> ")
            preco_de_vendas = input("Qual o preço de vendas? >>> ")
            estoque = input("Qual a quantidade de estoque? >>> ")
            quantidade_vendida = input("Qual a quantidade vendida? >>> ")
            marca = input("Qual a marca do produto? >>> ")
            garantia = input("Qual a garantia do produto? >>> ")
            categoria = input("Qual a categoria do produto? >>> ")

            sql = "INSERT INTO PRODUTO (NOME_DO_PRODUTO, CODIGO_DE_BARRA, PREÇO_DE_VENDA, ESTOQUE, QUANTIDADE_VENDIDA, MARCA, GARANTIA, CATEGORIA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (nome_do_produto, codigo_de_barras, preco_de_vendas, estoque, quantidade_vendida, marca, garantia, categoria))

        elif tabela.upper() == 'VENDAS':
            nome_do_produto = input("Qual o nome do produto? >>> ")
            codigo_de_barras = input("Qual o código de barras? >>> ")
            preco_de_venda = input("Qual o preço de venda? >>> ")
            estoque = input("Qual a quantidade de estoque? >>> ")
            quantidade_vendida = input("Qual a quantidade vendida? >>> ")
            marca = input("Qual a marca do produto? >>> ")
            categoria = input("Qual a categoria do produto? >>> ")

            sql = "INSERT INTO VENDAS (NOME_DO_PRODUTO, CODIGO_DE_BARRA, PREÇO_DE_VENDA, ESTOQUE, QUANTIDADE_VENDIDA, MARCA, CATEGORIA) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (nome_do_produto, codigo_de_barras, preco_de_venda, estoque, quantidade_vendida, marca, categoria))

        connector.commit()
        print(f"Dados inseridos na tabela {tabela.upper()} com sucesso!")

    except mysql.connector.Error as error:
        print(f"Erro ao inserir dados na tabela {tabela.upper()}: {error}")
        connector.rollback()
    finally:
        cursor.close()
        connector.close()


# Função do menu principal
def menuPrincipal():
    print("\n-- MENU PRINCIPAL --")
    print("1. Criar Tabela")
    print("2. Atualizar Dados")
    print("3. Deletar Dados")
    print("4. Procurar Dados")
    print("5. Inserir Dados")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criarTabela()
    elif opcao == "2":
        tabela = input("Digite o nome da tabela que deseja atualizar: ")
        atualizarDados(tabela)
    elif opcao == "3":
        tabela = input("Digite o nome da tabela que deseja deletar dados: ")
        atributo = input("Digite o nome do atributo para deletar: ")
        valor = input(f"Digite o valor correspondente ao atributo {atributo}: ")
        deletarDados(tabela, atributo, valor)
    elif opcao == "4":
        tabela = input("Digite o nome da tabela que deseja procurar: ")
        procurarDados(tabela)
    elif opcao == "5":
        tabela = input("Qual tabela deseja inserir dados (COMPRAS, ESTOQUE, PRODUTO, VENDAS)? >>> ")
        if tabela.upper() in ['COMPRAS', 'ESTOQUE', 'PRODUTO', 'VENDAS']:
            inserirDados(tabela)
        else:
            print("Tabela inválida. Operação de inserção cancelada.")
    elif opcao == "6":
        print("Saindo do programa...")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        menuPrincipal()

# Chamada da função menuPrincipal() para iniciar o programa
menuPrincipal()