"""
Repetições
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando o codigo não tem fim """


"""Atividade minha para fortalecer a mente
Escreva um codigo que conte até 100 OK
Depois faça o programa quebrar com 70 fazendo ele pular do 30 a 50 sem contar"""

contador = 0 

while contador <= 100:
    contador += 1
    if contador == 5:
        print('não quero mostrar o', contador)
        continue
    if contador >= 10 and contador <= 30:
        print('Não quero mostrar o', contador)
        continue

    print(contador)

    if contador == 70:
        break
    
print("Acabou")