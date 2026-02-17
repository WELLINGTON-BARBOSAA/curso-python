#Crie um programa com:

#1) Uma função chamada verificar_numero(numero)

#Essa função deve:
#Receber um número

#Retornar:

#"Par" se o número for par
#"Ímpar" se o número for ímpar

#2) No programa principal:

#Peça ao usuário para digitar um número
#Chame a função
#Mostre o resultado na tela

def verificar_numero(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar' 

usuario = int(input('Digite um numero: '))
par_impar = verificar_numero(usuario)
if usuario % 2 == 0:
    print(f'O numero digitado foi {usuario}, ele  é PAR')

else:
    print(f'Esse numero digitado foi {usuario}, ele é ÍMPAR')