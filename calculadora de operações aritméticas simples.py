print("Calculadora de operações aritméticas simples")
print("Selecione a operação desejada:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Digite o número da operação (1/2/3/4): ")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if operacao == '1':
    resultado = numero1 + numero2
    print(f"\nResultado: {numero1} + {numero2} = {resultado}")

elif operacao == '2':
    resultado = numero1 - numero2
    print(f"\nResultado: {numero1} - {numero2} = {resultado}")

elif operacao == '3':
    resultado = numero1 * numero2
    print(f"\nResultado: {numero1} × {numero2} = {resultado}")

elif operacao == '4':
    
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"\nResultado: {numero1} ÷ {numero2} = {resultado}")
    else:
        print("\nErro: não é possível dividir por zero")

else:
    print("\nInfelizmente a operação escolhida é inválida. Por favor, escolha outra opção e tente novamente.")
