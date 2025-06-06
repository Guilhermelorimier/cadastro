def cadastrar_nome(cadastro):
    try:
        novo_nome = input("Digite o nome da pessoa: ")
        cadastro.append(novo_nome)
        print(f"Usuário {novo_nome} foi adicionado.")
    except Exception as e:
        print(f"Erro ao cadastrar nome: {e}")

def listar_nome(cadastro):
    try:
        print("\nLista de nomes cadastrados:")
        if not cadastro:
            print("Nenhum nome cadastrado.")
        else:
            for i, nome in enumerate(cadastro, start=1):
                print(f"{i}. {nome}")
    except Exception as e:
        print(f"Erro ao listar nomes: {e}")

def excluir_nome(cadastro):
    try:
        excluir_nome = input("Digite o nome para excluir: ")
        if excluir_nome in cadastro:
            cadastro.remove(excluir_nome)
            print(f"{excluir_nome} foi removido.")
        else:
            print("Nome não encontrado.")
    except Exception as e:
        print(f"Erro ao excluir nome: {e}")

def menu():
    cadastro = []
    while True:
        try:
            print("\n---------SISTEMA DE CADASTRO-----------")
            print("[1] Cadastrar nome")
            print("[2] Listar nomes")
            print("[3] Excluir nome")
            print("[0] Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                cadastrar_nome(cadastro)
            elif opcao == '2':
                listar_nome(cadastro)
            elif opcao == '3':
                excluir_nome(cadastro)
            elif opcao == '0':
                print("Saindo...")
                break
            else:
                print("!!! Opção inválida. Tente novamente. !!!")
        except Exception as e:
            print(f"Erro no menu: {e}")

menu()