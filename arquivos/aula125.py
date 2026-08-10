# Atributos de Classes


# Também poderia colocar aqui uma CONSTANTE, já que o ano atual não muda

class Pessoa:
    ano_atual = 2026 # não é muito normal utilizar isso, mas pode acontecer

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nasc(self):
        return self.ano_atual - self.idade

p1 = Pessoa('Wellington', 31)
p2 = Pessoa('Eduarda', 25)

print(p1.get_ano_nasc())
print(p2.get_ano_nasc())

