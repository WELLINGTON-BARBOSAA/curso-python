'''
Repetições
while (enquanto)
Executa uma ação enquanto a condição for verdadeira'''

condicao = True

while condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'Sair':
        break

# Crtl + C é um comando que interrompe o programa quando aparece em loop infinito