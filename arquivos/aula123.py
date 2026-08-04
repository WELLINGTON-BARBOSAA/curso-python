# Escopo da classe e metodos da classe


class Animal:
    def __init__(self,nome):
        self.nome = nome

    variavel = 'Qualquer coisa'
    print(variavel) # essa variavel só funciona dentro do __init__, fora dela não tem funcionalidade
    print(variavel)

    def Comendo(self, alimento):
        print(f'O leao esta comendo uma maça {alimento}')
    
leao = Animal('Leão')
print(leao.nome)
leao.Comendo('Maça')