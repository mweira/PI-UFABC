"""# Exercício 2

Faça um programa que simule o lançamento de uma moeda, sorteando um número aleatório entre 0 e 1 (pesquise sobre a função `random`, da biblioteca `random`). Se o número sorteado for menor ou igual a 0.5, imprima "cara" e se for maior "coroa".
"""

import random 

n1 = random.random()

print(n1)

if n1 <= 0.5: 
  print("cara")
else: 
  print("coroa")
