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