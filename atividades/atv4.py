' Faça um Programa que peça as 4 notas bimestrais e mostre a média. '

nota1= input('Nota do primeiro bimestre: ')
nota2= input('Nota do segundo bimestre: ')
nota3= input('Nota do terceiro bimestre: ')
nota4= input('Nota do quarto bimestre: ')

not1 = float(nota1)
not2 = float(nota2)
not3 = float(nota3)
not4 = float(nota4)

media = (not1 + not2 + not3 + not4) / 4


if media <= 7:
    print('Você esta REPROVADO')
else:
    print('Voce está APROVADO')

#Aprovado
#Reprovado

print(f'Sua média é de: {media:.1f} ')