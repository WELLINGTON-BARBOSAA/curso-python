# Faça um Programa que calcule a área de um quadrado, 
# em seguida mostre o dobro desta área para o usuário.

area_quadrado = float(input('Digite o valor de uma area: '))
areaQ_calculada = area_quadrado * area_quadrado
areaQ_dobro = areaQ_calculada * 2

print(f'Sua area digitada foi: {area_quadrado}')
print()
print(f'Sua area calculada foi: {areaQ_calculada:.2f} cm²')
print()
print(f'Sua area digitada foi: {areaQ_dobro:.2f} cm²')
