'''👉 Criar 1 projeto simples (ex: calculadora, lista de tarefas, simulador, cronômetro).
📝 Nomeie o arquivo como “projeto-dia8” e salve no GitHub.'''


# Vou precisar de duas variaveis para colocar os numeros

print('-' *30)
print(  'SEJA BEM VINDO A SUA CALCULADORA BÁSICA')
print('-' *30)
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite o segundo numero: '))
operador_digitado = input('Digite o operador desejado: ')


if operador_digitado == '*':
    print(f'O resultado da sua multiplicação é  :{numero1*numero2}')
elif operador_digitado == '-':
    print(f'O resutado da sua subtração é : {numero1-numero2}')
elif operador_digitado == '+':
    print(f'O resultado da sua adição é : {numero1+numero2}')
elif operador_digitado == '/':
    print(f'O resultado da sua divisão é: {numero1/numero2}')
else:
    print('Você digitou algo errado')

print('-' *30)
print(  'CALCULADORA ENCERRADA ')
print('-' *30)