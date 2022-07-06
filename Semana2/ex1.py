"""""
# Exercício 1

Faça um programa que receba dois números e, usando condicionais, mostre o maior. Se por acaso os dois números forem iguais, imprima a mensagem "Números iguais".
"""

n1 = input("Digite o primeiro número : ")
n2 = input("Digite o segundo número : ")

if n1>n2: 
  print("O primeiro número é maior que o segundo")
elif n1 == n2: 
  print("Ambos são iguais")
else: 
  print("O segundo número é maior que o primeiro")