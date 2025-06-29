import random 

def exibir_menu():
    print("\n===== SORTEADOR DE ALUNOS =====")
    print("1 - Sortear um nome")
    print("2 - Mostrar lista de alunos")
    print("3 - Adicionar mais alunos")
    print("0 - Sair")

def sortear_nome(lista):
    if len(lista) == 0:
        print("A lista está vazia. Adicione nomes primeiro.")
    else:
        sorteado = random.choice(lista)
        print(f"\n O aluno sorteado foi: {sorteado}")

def mostrar_lista(lista):
    if len(lista) == 0:
        print("A lista está vazia.")
    else:
        print("\n Lista de alunos:")
        for i, nome in enumerate(lista, start=1):
            print(f"{i}. {nome}")

def adicionar_nomes(lista):
    print("\nDigite os nomes dos alunos (digite 'x' para encerrar):")
    while True:
        nome = input("Nome do aluno: ").strip()
        if nome.lower() == 'x':
            break
        elif nome == '':
            print("Nome vazio! Tente novamente.")
        else:
            lista.append(nome)
            print(f"Aluno '{nome}' adicionado.")

alunos = []

# Primeiro passo: pedir que o usuário adicione nomes
print("Bem-vindo ao sistema de sorteio!")
adicionar_nomes(alunos)

# Loop principal
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        sortear_nome(alunos)
    elif opcao == "2":
        mostrar_lista(alunos)
    elif opcao == "3":
        adicionar_nomes(alunos)
    elif opcao == "0":
        print("Encerrando o programa... Até logo!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
