alunos = []

def cadastrar_aluno():
    nome = input("Nome: ")
    email = input("Email: ")
    curso = input("Curso: ")
    aluno = {"nome": nome, "email": email, "curso": curso}
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    for i, aluno in enumerate(alunos):
        print(f"{i+1}. {aluno['nome']} - {aluno['email']} - {aluno['curso']}")

def menu():
    while True:
        print("\n=== Sistema de Alunos ===")
        print("1 - Cadastrar novo aluno")
        print("2 - Listar alunos")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            break
        else:
            print("Opção inválida! Por favor, tente novamente.")

menu()
