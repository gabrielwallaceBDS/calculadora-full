import time
#calculadora
def linha():
    print('~~'*15)




#programa principal
linha()
print('''
Calculadora Pro
[1] - adiçao  
[2] - subtrçao   
[3] - divisao 
[4] - vezes
[5] - x² elevado 
[0] - sair
''')
option = 9
while option != 0:
  option = int(input('digite a opçao desejada: '))
  linha()
  if option == 0:
    print('Programa encerrado')
    break
  numero1 = int(input('digite um numero: '))
  numero2 = int(input('digite o segundo numero: '))
  if option == 1:
    print('SOMA DOS VALORES.')
    print(numero1+numero2)
  if option == 2:
    print('SUBTRAÇAO DOS VALORES.')
    print(numero1-numero2)
  if option == 3:
    print('DIVISAO DOS VALORES')
    print(numero1/numero2)
  if option == 4:
    print('MULTILICAÇÃO DE VALORES')
    print(numero1*numero2)
  if option == 5:
    print('ELEVADO A X')
    print((numero1**numero2))
  

