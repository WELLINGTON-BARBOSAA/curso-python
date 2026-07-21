# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome, bairro, cidade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.bairro = bairro
        self.cidade = cidade

p1 = Pessoa('Wellington', 'Barbosa', 'Morro Doce', 'São Paulo')
print(p1.nome)
print(p1.sobrenome)
print(p1.bairro)
print(p1.cidade)
print()

p2 = Pessoa('Eduarda', 'Porto', 'Centro', 'Guarulhos')
print(p2.nome)
print(p2.sobrenome)
print(p2.bairro)
print(p2.cidade)
print()

p3 = Pessoa('Jose', 'Fialho', 'Centro', 'São João do Piaui')
print(p3.nome)
print(p3.sobrenome)
print(p3.bairro)
print(p3.cidade)
print()

p4 = Pessoa('Raimunda', 'de Sousa', 'São Sebastião', 'sSão João do Piaui')
print(p4.nome)
print(p4.sobrenome)
print(p4.bairro)
print(p4.cidade)