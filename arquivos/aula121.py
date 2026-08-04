# Metodos em instâncias de classes Python

#  Metodos de instâncias, ou seja, cada instância vai ter seu proprio metodo
# mas os dados são diferentes para cada instância

# Classe --> é o molde ou projeto
# Objeto --> é uma instância criada a partir da classe
# Atributos --> São as caracteritisca de um objeto
# Metodos -->  São ações que o objeto pode realizar (como falar() ou latir())
# self --> representa a propria instância do objeto, permitindo acessar e armazenar seus atributos.

class Carro:
    def __init__(self, nome, marca):
        self.cor = nome
        self.marca = marca

    def acelerar(self):
        print(f'{self.nome} esta acelerando')

celta = Carro('Celta', 'Ford')
print(celta.nome)
print(celta.marca)
celta.acelerar()

fusca = Carro('Fusca', 'Ford')
print(fusca.nome)
print(fusca.marca)
fusca.acelerar()
