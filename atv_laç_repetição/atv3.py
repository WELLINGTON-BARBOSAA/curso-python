''' 3. Faça um programa que leia e valide as seguintes informações: 
a. Nome: maior que 3 caracteres; 
b. Idade: entre 0 e 150; 
c. Salário: maior que zero; 
d. Sexo: 'f' ou 'm'; 
e. Estado Civil: 's', 'c', 'v', 'd'; 
Use a função len(string) para saber o tamanho de um texto (número de caracteres).'''

def nome_valido (nome):
    if not len(nome) > 3:
        return # return vazio é = None
    return nome   

def idade_valida(idade):
    if idade > 150:
        return
    return idade

def salario_valido(salario):
    if not salario > 0:
        return 
    return salario

def sexo_valido (sexo):
    if not sexo in ('m', 'f'):
        return 
    return sexo

def estado_valido(civil):
    if not civil in ('s', 'c', 'd', 'v'):
        return
    return civil

while True:

    nome = input('Digite seu nome: ')
    if nome_valido(nome): # if automaticamente checa se é verdadeiro. 
        print('Nome valido')
    else:
        print('Nome invalido')

    idade = int(input('Digite sua idade: '))
    if idade_valida(idade):
        print('Idade valida')
    else:
        print('Idade incorreta, tente novamente')


    salario = int(input('Digite seu salario: ') )
    if salario_valido (salario):
        print('Salario valido')
    else:
        print('Salario invalido, tente novamente')


    sexo = input('Digite seu sexo: ').lower()
    if sexo_valido(sexo):
        print('Sexo validado')
    else:
        print('Sexo invalido, tente novamente')


    civil = input('Digite seu estado civil: ').lower()
    if estado_valido (civil):
        print('Estado validado')
    else:
        print('Estado incorreto') 
    break
