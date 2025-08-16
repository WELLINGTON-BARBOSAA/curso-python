'Crie um programa que leai o nome completo de uma pessoa e mostre'
' - O nome com todas as letras maiusculas e minusculas'
' - Quantas letras ao todo (sem contar com os espaços)'
' - Quantas letras tem o primeiro nome'


# nome = input('Digite seu nome completo: ')


nome = str(input('Digite seu nome completo: ')).strip() # para cortar o espaço ant/dep para evitar que o usuario faça
print('Analisando seu nome...')
nome_sem_espaço = nome.replace(' ', '')
print(f'Seu nome completo é de {len(nome_sem_espaço)} letras' )
print(f'Seu nome em letra minuscula é assim: {nome.lower()}')
print(f'Seu nome em letra maiuscula é assim: {nome.upper()}')
primeiro_nome = nome.split()[0] # separa as letras removendo espaços e com a [0] marca de onde vai começar
ultimo_nome = nome.split()[-1] # [-1] pega sempre o ultimo item do indice 
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras.')
print(f'Seu ultimo nome é {ultimo_nome} e possui {len(ultimo_nome)} letras')

