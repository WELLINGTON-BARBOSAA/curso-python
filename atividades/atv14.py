# Faça um Programa que calcule a área de um quadrado, 
# em seguida mostre o dobro desta área para o usuário.

area = float(input('Digite o valor de uma area: '))
area_calculada = area * area
area_dobro = area_calculada * 2

print(f'Sua area digitada foi: {area}')
print()
print(f'Sua area calculada foi: {area_calculada:.2f} cm²')
print()
print(f'Sua area digitada foi: {area_dobro:.2f} cm²')
