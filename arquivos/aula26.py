''' 
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número aparecer antes dos zeros
Sinal - + ou - 
Ex.: 0>-100, .1f
Conversion flags - !r !s !a
'''
variavel = 'ABC'
print(f'{variavel:!>10}')
print(f'{variavel:.<10}')
print(f'{variavel:$^10}')
# Para utilizar variavel:$^10 #colado e sem espaço

print(f'{8888888.5000:.2f}')
print(f'{8888888.5000:+.2f}')
# Colocando 5000:+.2f mostra ao terminal que eu quero ver o numero positivo
# Colocando 5000:-.2f mostra ao terminal que eu quero ver o numero negativo
print(f'{8888888.5000:-.2f}')

#
print(f"O hexadecimal de 1500 é {1500:08X}")
