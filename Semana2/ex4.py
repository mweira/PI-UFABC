"""# Exercício 4

Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela
que considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários
com menor salário terão um aumento proporcionalmente maior do que os funcionários
com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus adicional de salário. Faça um programa que leia:


- o valor do salário atual do funcionário;
- o tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).


Use as tabelas a seguir para calcular o salário reajustado deste funcionário e imprima o
valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha direito
a nenhum aumento.

|Salário Atual | Reajuste |  
|-------------:|---------:|
| até 1.500,00 |  25%     |
| até 2.500,00 |  20%     |
| até 3.500,00 |  15%     |
| até 5.000,00 |  10%     |
| acima de 5.000,00 | sem aumento |

| Tempo de Serviço  | Bônus  |
|------------------:|-------:|
| menos de 3 anos   | sem bonus |
| de 3 a 5 anos     | 200,00    |
| de 5 a 8 anos     | 300,00    |
| de 8 a 10 anos    | 400,00    |
| acima de 10 anos  | 500,00    |


"""

n1 = int(input("Qual o seu salário atual ? "))

if n1 < 1500:
  n2 = n1 + (1/4)*n1
elif n1 >= 1500 and n1 < 2500: 
  n2 = n1 + (1/5)*n1
elif n1 >= 2500 and n1 < 3500: 
  n2 = n1 + (3/20)*n1
elif n1 >= 3500 and n1 < 5000: 
  n2 = n1 + (1/10)*n1
else: 
  print("Não há aumento")

print(n2)

n3 = int(input("Quanto tempo de contribuição você possui ? "))

n4 = 0

if n3 < 3: 
  print("Não há bônus")
elif n3>=3 and n3<5: 
  n4 = n4 + 200
elif n3>=5 and n3<8: 
  n4 = n4 + 300
elif n3>=8 and n3<10: 
  n4 = n4 + 400 
else: 
  n4 = n4 + 500

print(n4)

salario = n2+n4

print(salario)
