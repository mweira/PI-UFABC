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