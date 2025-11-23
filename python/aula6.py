'''📝Dia 10 – Missão:
Trabalhar com listas.
Criar um código que percorra uma lista e exiba resultados formatados.'''

minha_lista = ['Wellington', 'Jose', 'Maria', 'Antonio', 'Fernanda']
minha_lista.append('Raimunda')

for i, nome in enumerate(minha_lista, start=1):
    print(f'{i} - {nome}')