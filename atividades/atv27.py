'''Faça um programa que leia a largura e altura de uma parede em metros
Calcule a sua area e a quantidade de tinta necessaria para pinta la 
sabendo que cada litro de tinta pinta uma area de 2m²'''

# largura = float(input('Qual é a largura da parede: '))
# altura = float(input('Qual altura da parede: '))
# cal_area = altura * largura
# print(f'As medidas são {largura} x {altura}, sua area calculada é de : {cal_area:.2f} M²')
# tinta = cal_area / 2
# print(f'Será necessario {tinta}L de tinta para pintar area.')

def area (altura, largura):
    return altura *  largura

while True:
    try:
        cal_altura = float(input('Digite a altura: '))
        cal_largura = float(input('Digite a largura: '))
        formula = area(cal_altura,cal_largura)
        print(f'O calculo da area é de {formula:.2f} M²')
        tinta = formula/2
        print(f'Sera necessario {tinta:.2f}L para pintar a parede')
        break

    except Exception:
            print('Voce não digitou numero, tente novamente')
