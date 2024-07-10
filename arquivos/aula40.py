""" Calculadora com while"""

while True: 
    num_1 = input ('Digite um numero: ')
    num_2 = input ('Digite outro numero: ')
    operador = input('Digite um operador: ')

    numero_valido1 = 0
    numero_valido2 = 0

    numeros_validos = None

    try:
        numero_valido1 = int(num_1)
        numero_valido2 = int(num_2)
        numeros_validos = True

    except:
        numeros_validos is None
    
    if numeros_validos is None:
        print('Um ou dois numeros digitados são invalidos ')
        continue

    operador_valido = '+-*/'

    if operador not in operador_valido:
        print('Voce não digitou um operador, tente novamente')
        continue

    if len(operador) > 1:
        print("digite apenas um operador")

    if operador == '+':
        print(numero_valido1+numero_valido2)
    elif operador == '-':
        print(numero_valido1-numero_valido2)
    elif operador == '*':
        print(numero_valido1*numero_valido2)
    elif operador == '/':
        print(numero_valido1/numero_valido2)
    else:
        print('Algo deu errado na conta')

    sair = input('Voce deseja [S]air?' ).lower().startswith('s')
    if sair is True:
        break