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