' Faça um Programa que peça as 4 notas bimestrais e mostre a média. '

nota1= float(input('Nota do primeiro bimestre: '))
nota2= float(input('Nota do segundo bimestre: '))
nota3= float(input('Nota do terceiro bimestre: '))
nota4= float(input('Nota do quarto bimestre: '))

media = (nota1 + nota2 + nota3 + nota4) / 4


if media <= 7:
    print('Você esta REPROVADO')
else:
    print('Voce está APROVADO')

print(f'Sua média é de: {media:.1f} ')