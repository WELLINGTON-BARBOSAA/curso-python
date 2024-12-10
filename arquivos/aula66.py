''' Argumentos nomeados e não nomeador em funções Pytnhon
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)'''

# def soma(x, y, z): # argumento posicional 
#     print(f'{x=} y={y}', '|', 'x + y = ', x + y)

# soma(1, 2, 3)
# soma(2, y= 14, z=1) # Argumentos nomeados é quando da uma atribuição ao argumento. Quando faz isso, é regra nomear todos a frente  



def calculadora (a, b, c):
    print(f'O resultado da conta é: {a + b / c}' )

calculadora(1, 7, 8)
calculadora(5, 10, 8)
calculadora(1, 85, 8)
calculadora(1, 30, 8)
calculadora(1, 100, 8)
calculadora(6, 7, 8)
calculadora(250, 7, 8)
calculadora(1, 300, 8)
calculadora(1, 7, 800)
