"""
Repetições
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando o codigo não tem fim """



quantidade_linha = 10
quantidade_coluna = 10

linha = 0
while linha <= quantidade_linha:
    coluna = 0
    while coluna <= quantidade_coluna:
        coluna += 1
        print(f"{linha=} {coluna=}")
    linha += 1

print('Acabou')






