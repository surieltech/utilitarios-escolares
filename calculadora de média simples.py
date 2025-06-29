# Calculadora de média simples

nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"\nA média de {nome} é: {media:.3f}")

if media >= 7:
    print("Situação: Aprovado")
elif media >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")
