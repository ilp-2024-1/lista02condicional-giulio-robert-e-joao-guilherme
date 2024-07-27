#Questão 01

# salario = float(input('Declare seu salário:'))
# isento = float(1903.98)
# porcentagem1 = 7.5 / 100
# porcentagem2 = 15 / 100
# porcentagem3 = 22 / 100
# porcentagem4 = 27.5 / 100

# if salario <= isento:
#     print('Você está isento do imposto de renda!')
# elif salario <= 2826.65:
#     imposto = salario * porcentagem1
#     print(f'O seu imposto é de {imposto}')
# elif salario <= 3751.05:
#     imposto = salario * porcentagem2
#     print(f'O seu imposto é de {imposto}')
# elif salario <= 4664.68:
#     imposto = salario * porcentagem3
#     print(f'O seu imposto é de {imposto}')
# else:
#     imposto = salario * porcentagem4
#     print(f'O seu imposto é de {imposto}')
# print('Cuidado com o leão...')

#Questão 02


ano = int(input("Digite uma data: "))

if ano % 4 == 0 and ano % 100 != 0:
    print("Esse ano é bissexto")
else:
    print("Esse ano não é bissexto")

#Questão 03

# numero_solicitado = int(input('Digite um número entre 1 e 10:'))

# if numero_solicitado >= 1 and numero_solicitado <= 10:
#     print('O número digitado está DENTRO da faixa solicitada')
# else:
#     print('O número digitado está FORA da faixa solicitada')

#questão 04
valor = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))

if valor < valor2:
    print("Esse valor é o maior: ", valor2)
elif valor2 < valor:
    print("Esse valor é o maior: ", valor)

#Questão 05

# import random

# numeroaleatorio1 = random.randint(1, 500)
# numeroaleatorio2 = random.randint(1, 500)

# if numeroaleatorio1 > numeroaleatorio2:
#     diferença = numeroaleatorio1 - numeroaleatorio2
#     print(f'A diferença do primeiro número para o segundo é:{diferença}')
# elif numeroaleatorio2 > numeroaleatorio1:
#     diferença = numeroaleatorio2 - numeroaleatorio1
#     print(f'A diferença do segundo número para o primeiro é:{diferença}')
# else:
#     print('Os números são iguais')

#Questão 06

03 

valor = int(input("Digite um valor:"))
valor_1 = int(input("Digite um valor:"))
valor_2 = int(input("Digite um valor:"))

if valor < valor_1 < valor_2:
    print(valor, valor_1, valor_2)

elif valor_1 < valor < valor_2:
    print(valor_1, valor,valor_2)

elif valor_1 < valor_2 < valor:
    print(valor_1, valor_2, valor)

elif valor_2 < valor < valor_1:
    print(valor_2,valor, valor_1)

elif valor < valor_2 < valor_1:
    print(valor,valor_2,valor_1)

elif valor_2 < valor_1 < valor:
    print(valor_2,valor_1,valor)


#Questão 07

a = int(input('Digite um número:'))
b = int(input('Digite um número:'))
c = int(input('Digite um número:'))

desejo = input('Deseja ver os valores em ordem crescente ou descrescente?')

if c > b > a and desejo == 'decrescente' or c < b < a and desejo == 'crescente':
    print(c, b, a)
elif c > a > b and desejo == 'decrescente' or c < a < b and desejo == 'crescente':
        print(c, a, b)
elif b > c > a and desejo == 'decrescente' or b < c < a and desejo == 'crescente':
        print(b, c , a)
elif b > a > c and desejo == 'decrescente' or b < a < c and desejo == 'crescente' :
        print(b, a, c)
elif a > c > b and desejo == 'decrescente' or a < c < b and desejo == 'crescente' :
        print(a, c, b)
elif a > b > c and desejo == 'decrescente' or a < b < c and desejo == 'crescente' :
        print(a, b, c)

#Questão 08

valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite um valor: "))
valor3 = int(input("Digite um valor: "))

if valor1 == valor2 and valor1 == valor3 and valor2 == valor3:
    print("esse triangulo é equilátero")
elif valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
    print("esse trangulo é isósceles")
elif valor1 != valor2 and valor1 != valor3 and valor2 != valor3:
    print("esse triangulo é escaleno")





