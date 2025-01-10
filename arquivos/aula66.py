''' Argumentos nomeados e não nomeador em funções Pytnhon
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)'''

# def soma(x, y, z): # argumento posicional 
#     print(f'{x=} y={y}', '|', 'x + y = ', x + y)

# soma(1, 2, 3)
# soma(2, y= 14, z=1) # Argumentos nomeados é quando da uma atribuição ao argumento. 
# Quando faz isso, é regra nomear todos a frente  



# def conta (a, b, c):
#     print(f'{a * b * c}')

# conta(1,8,9)
# conta(10,8,9)
# conta(1,88,9)
# conta(1,8,93)
# conta(1,85,9)

def letras (x, y, z):
    print(f'{x} {y} {z}', '|', 'x + y + z = ', x + y + z)

letras(1,2,3)
letras(4,5,8)