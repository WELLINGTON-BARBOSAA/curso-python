contador = 0 

while contador <= 10:
    contador += 1
    if contador >= 5 and contador <= 8:
        print(f'Não quero mostrar o numero {contador}')
        continue
    print(contador)