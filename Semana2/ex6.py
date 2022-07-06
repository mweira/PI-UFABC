"""# Exercício 6

Sejam $a$ e $b$ os catetos de um triângulo retângulo, onde a hipotenusa  ́e obtida pela e:
$hipotenusa = \sqrt{a^2 + b^2}$. Faça uma funçãoo que receba os valores de $a$ e $b$, calcule e retorne o valor da hipotenusa através da equação.

Fora da função, faça um programa que leia os valores de $a$ e $b$, e imprima o valor da $hipotenusa$.
"""

import math

def formula(a, b):
  return math.sqrt(a*a + b*b)

a = int(input("Digite um valor para o cateto "))
b = int(input("Digite o valor do outro cateto "))

c = formula(a, b)

print("O valor da hipotenusa é ", c)
