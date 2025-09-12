'Faça um programa que leia um nome de usuário e a sua senha '
'e não aceite a senha igual ao nome do usuário, '
'mostrando uma mensagem de erro e voltando a pedir as informações. '

while True: 

    usuario = input('Digite sua usuario: ')
    senha = input('Digite sua senha: ')

    if usuario == senha: 
        print('Senha e usuario são iguais')
        print('Tente novamente')

    else:
        print('Deu tudo certo')
        break
