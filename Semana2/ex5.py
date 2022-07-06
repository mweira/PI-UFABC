"""# Exercício 5

Faça uma função para verificar se um número passado como parâmetro ́e zero, positivo ou negativo. Se o número for positivo, a função deve retornar 1, se for negativo, retornar -1, e se for 0, retornar 0. 

Inclua também código (fora da função) que leia um número digitado pelo usuário, faça uma chamada para a função, e imprima as mensagens:

- Número digitado é negativo
- Número digitado é positivo
- Número digitado é zero

de acordo com o retorno da função.
"""

def verifica(x): 
  if x==0:
    return ("0") 
  elif x>0: 
    return("1")
  else: 
    return("-1")

x = int(input("Digite o valor "))

res = verifica(x)

print(res)

if x==0: 
  print("Número digitado é zero")
elif x>0: 
  print("Número digitado é positivo")
else: 
  print("Número digitado é negativo")
