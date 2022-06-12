# Exercício 1

Faça um programa que peça um número e armazene-o em uma variável. A seguir, mostre a mensagem "O número informado foi [número]"
"""

n1 = input("Digite um número : ")
print("O número informado foi",n1)

"""# Exercício 2

Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
Dica: para usar o valor de $\pi$, pesquise por `math.pi`.
"""

import math

n1 = float(input("Digite um valor para o raio do círculo : "))
n2 = math.pi*(math.pow(n1, 2))
print("A área do círculo é : ", n2)

"""# Exercício 3

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

   - o produto do dobro do primeiro com metade do segundo .
   - a soma do triplo do primeiro com o terceiro.
   - o terceiro elevado ao cubo. 
"""

import math

n1 = int(input("Digite um número inteiro "))
n2 = int(input("Digite outro número inteiro "))
n3 = float(input("Digite um número real "))

n4 = (n1*2) * (n2/2)
n5 = (n1*3) + n3
n6 = math.pow(n3, 3)

print("O produto do dobro do primeiro com metade do segundo : ", n4)
print("A soma do triplo do primeiro com o terceiro : ", n5)
print("O terceiro elevado ao cubo : ", n6)

"""# Exercício 4

Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas na semana. Calcule e mostre o total do seu salário ao final de 4 semanas. 
"""

n1 = int(input("Quantas horas você trabalha por semana ? "))
n2 = float(input("Quanto você ganha por hora ? "))
n3 = n1*n2*4

print("O seu salário ao final de 4 semanas é de R$", n3)

"""# Exercício 5

Faça um programa que leia um número inteiro qualquer e que apresete, além do número informado, o seu antecessor e do seu sucessor.
"""

n1 = int(input("Digite um número : "))

print("O número digitado foi : ", n1)
print("Seu antecessor é : ", n1-1)
print("Seu sucessor é : ", n1+1)

"""# Exercício 6

Faça um programa que leia quatro notas, e seus respectivos pesos, e que apresente a média final simples e a média final ponderada.
"""

n1 = float(input("Digite a primeira nota : "))
n2 = float(input("Digite a segunda nota : "))
n3 = float(input("Digite a terceira nota : "))
n4 = float(input("Digite a quarta nota : "))

p1 = float(input("Digite o peso da primeira nota : "))
p2 = float(input("Digite o peso da segunda nota : "))
p3 = float(input("Digite o peso da terceira nota : "))
p4 = float(input("Digite o peso da quarta nota : "))

media_simples = (n1+n2+n3+n4)/4
media_ponderada = ((n1*p1) + (n2*p2) + (n3*p3) + (n4*p4))/(p1+p2+p3+p4)

print("Sua média final simples foi : ", media_simples)
print("Sua média final ponderada foi : ", media_ponderada)

"""# Exercício 7

Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 12 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 
"""

metros_quadrados = int(input("Digite o número de metros quadrados da área a ser pintada : "))
litros = metros_quadrados*(1/12)
latas = litros/18
preco = latas*80

print("A localidade possui : ", metros_quadrados, " metros quadrados")
print("Serão necessários : ", litros, " litros")
print("Serão necessárias : ", latas, " latas")
print("Será gasto R$", preco)
