'''
Repetições
while (enquanto)
Executa uma ação enquanto a condição for verdadeira'''

condicao = True

while condicao:
    nome = input('Digite seu nome completo: ')
    print(f'Seu nome completo é: {nome}')
    
    if nome == "Sair":
        break
print('Voce saiu do programa')


# Crtl + C é um comando que interrompe o programa quando aparece em loop infinito