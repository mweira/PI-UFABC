"""# Exercício 4

Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas na semana. Calcule e mostre o total do seu salário ao final de 4 semanas. 
"""

n1 = int(input("Quantas horas você trabalha por semana ? "))
n2 = float(input("Quanto você ganha por hora ? "))
n3 = n1*n2*4

print("O seu salário ao final de 4 semanas é de R$", n3)