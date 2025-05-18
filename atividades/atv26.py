# real = float(input('Digite quantos reais você tem: '))
# formula = real / 5.22
# print(f'Voce tem: US$ {formula:.2f}')

def moeda (real):
    return real / 5.22


while True:

     try: 
         valor_real = float(input('Digite o valor em real: '))
         valor_dolar = moeda(valor_real)
         print(f'Seu valor em dolar é US$ {valor_dolar:.2f}')
         break
    
     except ValueError: 
         print('Você não digitou um numero, tente novamente')    