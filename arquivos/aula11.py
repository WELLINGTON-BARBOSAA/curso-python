# Ordem dos operadores 
# 1. (n + n) -> na programação é dado prioridade aos parenteses () é feito de dentro para fora
# 2. ** exponenciação 
# 3. */ // %
# 4. + -

conta1 = (1 + 1) ** (5 + 5)         #conta1 = 1 + 1 ** 5 + 5 Resultado deu 7 por causa da ordem
# dos operadores
print(conta1)

conta_1 = (5 + 5) // (1 + 1) 
conta_2 = (1 + 1) ** (5 + 5) 
conta_3 = (5 + 5) - (1 + 1) 

print(conta_1)
print(conta_2)
print(conta_3)