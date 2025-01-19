'''Faça um Programa que converta metros para centímetros. '''

metros = input('Digite o metro: ')

metros_conv = float(metros)

convr_m_em_cm = float (metros_conv* 100)
print(f'Você digitou {metros_conv} e convertendo para cm fica: {convr_m_em_cm:.2f} cm')