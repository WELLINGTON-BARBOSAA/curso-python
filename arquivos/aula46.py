for i in range(10):  # Aqui a contagem vai de 0 a 9
    if i == 2:
        print('Pulando o numero 2')
        continue

    if i == 8:
        print('O else não será executado')
        break       # Quando se encontra break o else não é executado

    for j in range(1, 3):       # Aqui indica que o numero 1 é o inicio e o 3 é o fim
        print(i, j)

else: 
    print('Laço completado')
