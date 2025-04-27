'''Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF'''


# F = C x 1,8 + 32

# temperatura = float(input('Digite a Temperatura: '))
# resultado = (temperatura * 1.8) + 32
# print(f'A °C {temperatura} em Fahrenheit é de: {resultado:.2f}F!')


def c_para_f(celsius):
    return celsius * 1.8 + 32

while True:
    try:
        celsius = float(input('Digite a temperatura em Celsius: '))
        fahrenheit = c_para_f(celsius)
        print(f'{fahrenheit}F!')
        break
    except ValueError:
        print('Algo está errado. Digite um número válido.')
