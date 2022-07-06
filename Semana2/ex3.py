"""# Exercício 3

Faca um programa que simule um "prova de matemática" para crianças que estão aprendendo a somar n  ́umeros inteiros menores do que 100. Sorteie um número aleatório entre 0 e 100 (procure pela função `randint` da biblioteca `random`), imprime esse número, e peça para o usuário digitar qual número precisa ser somado para completar 100. O seu programa deve verificar se o número digitado está correto ou não (isto é, se a soma do número sorteado com o digitado é igual a 100.
"""

import random 

n1 = random.randint(0, 100)

print("O valor aleatório é ", n1)

n2 = int(input("Digite o valor que deve ser somado para completar 100 : "))

if n1+n2 == 100: 
  print("O valor está correto")
else: 
  print("O valor está incorreto")
