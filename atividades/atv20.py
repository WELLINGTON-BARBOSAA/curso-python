'PROGRAMA QUE VAI CALCULAR A MEDIA DE 1 ALUNO (FUTURAMENTE FAREI DA TURMA TODA)'


aluno1 = input('Digite seu nome: ')

nota1= float(input('Digite sua primeira nota: '))
nota2= float(input('Digite sua segunda nota: '))
nota3= float(input('Digite sua terceira nota: '))
nota4= float(input('Digite sua quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print(f'A media do {aluno1} foi de {media}')
    print('VOCE PASSOU')

else:
    print(f'Sua média foi de {media}')
    print('REPROVADO') 

