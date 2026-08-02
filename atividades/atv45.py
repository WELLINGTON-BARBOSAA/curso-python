'''Jogo do JOKENPÔ'''

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0,2)
print('''Lembrando que:
      OPÇÃO [0] PEDRA 
      OPÇÃO [1] PAPEL 
      OPÇÃO [2] TESOURA''')

jogador = int(input('Digite qual numero deseja: '))
print(f'Você jogou {itens[jogador]}')
print()
print(f'A maquina jogou {itens[maquina]}')

if maquina == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('VOCÊ GANHOU')
    elif jogador == 2:
        print('VOCÊ PERDEU')

elif maquina == 1:
    if jogador == 0:
        print('VOCÊ PERDEU')
    elif jogador == 1:
        print('EMPATOU')
    elif jogador == 2:
        print('VOCE GANHOU')

elif maquina == 2:
    if jogador == 0:
        print('VOCE GANHOU')
    elif jogador == 1:
        print('VOCE PERDEU')
    elif jogador == 2:
        print('EMPATOU')

else:
    print('VOCÊ NÃO DIGITOU NENHUM NUMERO ACIMA')

