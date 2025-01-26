

# def multiplicador (*args):
#     total = 1
#     for numero in args:
#         total *= numero    
#     return total



# resultado = multiplicador(1 , 2, 3, 4, 5, 6, 7, 8, 9)
# print(f'O resultado da conta é : {resultado}')



def par_impar (numero):
    multiplo_de2 = numero % 2 == 0
    if multiplo_de2:
        return f'{numero} é par' 
    return f'{numero} é impar'

print(par_impar(8))


