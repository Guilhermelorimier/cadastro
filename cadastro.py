def menu():
    cadastro = []
    while True:
        print("\n---------SISTEMA DE CADASTRO-----------")
        print("[1] cadastrar nome")
        print("[2] listar nomes")
        print("[3] escluir nome")
        print("[0] sair")
        opcao = input("escolha uma opcao")

        if opcao == '1':
            novo_nome = input("digite o nome da pessoa: ")
            cadastro.append(novo_nome)
            print(f"usuario {novo_nome}foi adicionado: ")
        elif opcao == '2':
            print("\nlista de nomes cadastrados:")
            for i, nome in enumerate(cadastro, start=1):
                print(f"{i}. {nome}")
        elif opcao == '3':
            excluir_nome = input("digite o nome para excluir:")
            if excluir_nome in cadastro:
                cadastro.remove(excluir_nome)
                print(F"{excluir_nome}foi removido.")
            else:
                print("nome não encontrado.")
        elif opcao == '0':
            print("saindo...")
            break
        else:
            print("!!! opcao invalida. Tente novamente.!!!")
menu()
