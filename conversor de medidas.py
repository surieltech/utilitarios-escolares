# Conversor de Medidas 

def converter_comprimento():
    print("\n--- Conversão de Comprimento ---")
    print("1 - Metros (m) para Centímetros (cm)")
    print("2 - Metros (m) para Quilômetros (Km)")
    print("3 - Centímetros (cm) para Metros (m)")
    print("4 - Quilômetros (Km) para Metros (m)")

    opcao = input("Escolha uma opção (1 a 4): ")
    valor = float(input("Digite o valor: "))

    if opcao == "1":
        print(f"{valor} metros = {valor * 100} centímetros")
    elif opcao == "2":
        print(f"{valor} metros = {valor / 1000} quilômetros")
    elif opcao == "3":
        print(f"{valor} centímetros = {valor / 100} metros")
    elif opcao == "4":
        print(f"{valor} quilômetros = {valor * 1000} metros")
    else:
        print("Opção inválida.")

def converter_peso():
    print("\n--- Conversão de Peso ---")
    print("1 - Quilogramas (Kg) para Libras (Lb)")
    print("2 - Libras (Lb) para Quilogramas (Kg)")

    opcao = input("Escolha uma opção (1 ou 2): ")
    valor = float(input("Digite o valor: "))

    if opcao == "1":
        print(f"{valor} kg = {valor * 2.20462:.2f} lb")
    elif opcao == "2":
        print(f"{valor} lb = {valor / 2.20462:.2f} kg")
    else:
        print("Opção inválida.")

def converter_temperatura():
    print("\n--- Conversão de Temperatura ---")
    print("1 - Celsius (C°) para Fahrenheit (F°)")
    print("2 - Fahrenheit (F°) para Celsius (C°)")

    opcao = input("Escolha uma opção (1 ou 2): ")
    valor = float(input("Digite a temperatura: "))

    if opcao == "1":
        resultado = (valor * 9/5) + 32
        print(f"{valor}°C = {resultado:.2f}°F")
    elif opcao == "2":
        resultado = (valor - 32) * 5/9
        print(f"{valor}°F = {resultado:.2f}°C")
    else:
        print("Opção inválida.")

# Menu principal
def menu():
    while True:
        print("\n==== CONVERSOR DE MEDIDAS ====")
        print("1 - Converter Comprimento")
        print("2 - Converter Peso")
        print("3 - Converter Temperatura")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            converter_comprimento()
        elif escolha == "2":
            converter_peso()
        elif escolha == "3":
            converter_temperatura()
        elif escolha == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

menu()
