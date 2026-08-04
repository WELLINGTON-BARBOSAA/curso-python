# Entendo self em classes Python
# Classes - Molde (sem dados)
# Instâncias da classe (objeto) - Tem dados
# Uma classe pode gerar varias instâncias.
# Na classe o self é a própria instância 

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def Acelerar(self):
        print(f'O carro {self.nome} esta acelerando demais')

fusca = Carro('Fusca')
print(f'O nome do carro é: {fusca.nome}')
fusca.Acelerar()

celta = Carro('Celta')
print(f'O nome do carro é: {celta.nome}')
celta.Acelerar()