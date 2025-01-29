''' 
Higher Order Functions - Funções que pode receber ou retornar outras funções  
First Class Functions - funções que são tratados como outro dado comum (str,int etc)
'''

# def saudacao (msg):
#     return msg

# saudacao2 = saudacao # usando funções como valor de variavel 

# v =(saudacao2('Bom dia'))
# print(v)
# #############################################################

# def saudacao (msg):
#     return msg 

# def executa (funcao, texto): # Dentro do escopo esta protegida
#     return funcao (texto)

# v = executa(saudacao, 'Bom dia')
# print(v)

# ##############################################################

def saudacao (msg, nome):
    return f'{msg}, {nome}!'

def executa (funcao, *args):
    return funcao(*args)


print(executa(saudacao, 'Bom dia', 'Wellington'))
print(executa(saudacao, 'Boa noite', 'Jose'))
print(executa(saudacao, 'Boa Tarde', 'Augusto'))
