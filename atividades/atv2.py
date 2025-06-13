'''Faça um Programa que peça um número 
e então mostre a mensagem O número informado foi [número]. '''

# numero=input('Digite um numero: ')
# print(f'O numero digitado foi: {numero}')

def numero (number):
    return number

while True:
    try:
        num_dig = int(input('Digite um numero: '))
        digitado = numero(num_dig)
        print(f'O numero digitado foi {digitado}')
        break
    except ValueError:
        print('Voce não digitou um numero')

