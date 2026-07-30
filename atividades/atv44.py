''' Elabore um programa que calcule o valor a ser pago por um
produto, considerando o seu preço normal e condição de pagamentos:
- a vista dinheiro/cheque: 10% de desconto
- a vista no cartao: 5% de desconto
- em ate 2x no cartao: preço normal
- 3x ou mais no cartão: 20% de juros '''

valor_compra = float(input('Qual foi o valor da sua compra: '))
print(f'O valor da sua compra foi de R$ {valor_compra:.2f}')
print('Qual vai ser a forma de pagamento')
print()
print('A vista/pix -> 1 <- (com 10 % de desconto)')
print('Cartao de crédito digite -> 2 <-')
print('A vista no cartão tem desconto de 5%, dividindo em 2x fica o preço normal e acima de 3x tem juros de 20%') 
print()
desconto10 = valor_compra * 10/100
desconto5 = valor_compra * 5/100
juros20= valor_compra * 20/100

forma_pagamento = int(input('Qual vai ser a forma de pagamento: '))

if forma_pagamento <= 0:
    print('Valor invalido')
elif forma_pagamento == 1:
    print(f'O valor da sua compra com o desconto de 10% deu R$ {valor_compra - desconto10:.2f}')
elif forma_pagamento == 2:
    quantidad_parcela = int(input('Deseja dividir em quantas vezes:'))

    if quantidad_parcela == 1:
        print(f'O valor da sua compra ficou no valor de {valor_compra - desconto5:.2f}')

    elif quantidad_parcela == 2:
        valor_parcela = valor_compra / quantidad_parcela
        print(f'O valor da parcela ficou de  {valor_parcela:.2f}')
        print(f'o valor da final da compra ao termino das parcelas é de {valor_compra:.2f}')

    elif quantidad_parcela >= 3:
        valor_final = valor_compra + juros20
        valor_parcela = valor_final / quantidad_parcela

        print(f'O valor das parcelas ficou de : {valor_parcela:.2f}')
        print(f'E o valor total da compra ficou de : {valor_final:.2f}')

    else:
        print('Forma de parcelamento invalida')

else:
    print('Forma de pagamento inválida')