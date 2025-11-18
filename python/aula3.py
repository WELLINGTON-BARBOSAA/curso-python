'''Praticar estruturas condicionais (if / else).
📝 Criar um código que simule uma decisão (ex: cálculo de nota, temperatura ou
acesso)'''

print('*' *30)
print(  '   CALCULADORA DE MEDIA')
print('*' *30)

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2 

if media < 5:
    print(f'Com essa média de {media:.1f}, você esta REPROVADO.')
    print('Estude mais!')

elif media < 7:
    print(f'Com essa média de {media:.1f}, você esta em RECUPERAÇÃO')

else:
    print(f'Com média de {media:.1f}, você esta APROVADO')

print('-' *30)
print(  '   CALCULADORA ENCERRADA')
print('-' *30)