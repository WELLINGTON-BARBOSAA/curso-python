# Try, except, else e finally

# a = 18
# b = 0
# c = a / b

# try: 
#     a = 18
#     b = 0
#     c = a / b
    
# except: 
#     print('Codigo funcionou')

#Erros são feitos para serem tratados e nao silenciados.
# Por isso esse exemplo é uma má conduta de programação

# (Parte 2) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e: # 'as' indica qual variavel jogar o erro. 'e' é a variavel que fica erro
    print(e.__class__.__name__) # __class__.__name__ = mostra a classe em questão e o nome dela.    print(e) # e ou error = variavel que recebe o erro
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error: 
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception: # Exception, exceção que trata todas as exceções
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')