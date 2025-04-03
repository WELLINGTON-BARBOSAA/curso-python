'''    3. Faça um programa que leia e valide as seguintes informações: 
        a. Nome: maior que 3 caracteres; 
        b. Idade: entre 0 e 150; 
        c. Salário: maior que zero; 
        d. Sexo: 'f' ou 'm'; 
        e. Estado Civil: 's', 'c', 'v', 'd'; 
       Use a função len(string) para saber o tamanho de um texto (número de caracteres).'''

nome = input('Digite sua nome: ')
idade = int(input('Digite sua idade:'))
salario = float(input('Digite seu salário: '))
sexo = input('Digite o sexo(f ou m): ')
est_civ = input('Digite estado civil (s,c,v ou d): ')

if len (nome) >=  3:
    print('Numero validado')

else: 
    print('Numero invalido, tente novamente: ')

if idade > 0 and idade <= 150:
    print('Idade valida')

else:
    print('Idade invalida')

if salario > 0 :
    print('Salario valido')

else:
    print('Salario  invalido')

if sexo in ('m', 'M', 's', 'S'): 
    print('Sexo validado com sucesso')
else:
    print('Sexo negado, ex(s ou m)')
 
if est_civ in ('s', 'c', 'v', 'd'): 
    print('Estado civil valido')

else:
    print('Estado civil invalido (ex: s, c, v ou d)')