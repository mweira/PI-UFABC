"""# Exercício 8

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 12 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

    - comprar apenas latas de 18 litros;
    - comprar apenas galões de 3,6 litros;
    - misturar latas e galões, de forma que o desperdício de tinta seja menor. 
    
Acrescente 10% de folga nos três casos (isto é, você deve adicionar 10% sobre o total de litros de tinta necessário) e sempre arredonde os valores para cima, isto é, considere latas cheias. 


"""

import math

metros_quadrados = float(input("Digite o número de metros quadrados da área a ser pintada : "))

litros = metros_quadrados/12 * 1.1

latas = math.ceil(litros/18)
preco = latas*80

galoes = math.ceil(litros/3.6)
preco2 = galoes*25

print("Você terá que comprar ", litros, " litro(s) de tinta")

print("Você terá gasto R$", preco, " caso compre latas de 18 litros")

print("Você terá gasto ", preco2, " caso compre galões de 3,6 litros")

latas_min = math.floor(litros/18)
sobra = litros - (latas_min *18)
galoes_sobra = math.ceil(sobra/3.6)

print("Misturando latas e galões, a quantidade de latas a ser comprada é",latas_min,"e de galões",galoes_sobra)
print("O preço total é R$",latas_min*80 + galoes_sobra*25)