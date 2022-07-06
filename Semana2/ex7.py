"""# Exercício 7

Crie uma função que receba dois números ($n_1$ e $n_2$) e uma letra.

- Se a letra passada como parâmetro for "A", a função deve retornar a média aritmética entre os dois $\left(\frac{n_1+n_2}{2}\right)$
- Se a letra passada como parâmetro for "G", a função deve retornar a média geométrica entre os dois $\left(\sqrt{n_1+n_2}\right)$
- Se a letra passada como parâmetro for "H", a função deve retornar a média harmônica entre os dois $\left(\frac{2}{\frac{1}{n_1}+\frac{1}{n_2}}\right)$
- Se for passada qualquer outra letra, a função deve retornar 0

Fora da função, faça um programa que leia os dois números e uma letra, e imprima o resultado da chamada da função.
"""

import math

def funcao(n1, n2, letra): 
  if letra == "A" or letra == "a": 
    return (n1+n2)/2
  elif letra == "G" or letra == "g":
    return math.sqrt(n1+n2)
  elif letra == "H" or letra == "h": 
    return 2/((1/n1) + (1/n2))
  else: 
    return ("0")

n1 = int(input("Digite o primeiro número "))
n2 = int(input("Digite o segundo número "))
letra = str(input("Digite a letra "))

a = funcao(n1, n2, letra)

print(a)
