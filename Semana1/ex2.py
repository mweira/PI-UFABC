"""# Exercício 2

Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
Dica: para usar o valor de $\pi$, pesquise por `math.pi`.
"""
import math

n1 = float(input("Digite um valor para o raio do círculo : "))
n2 = math.pi*(math.pow(n1, 2))
print("A área do círculo é : ", n2)