frase = 'Wellington'

# indice - usado para percorrer cada caractere da string frase.
indice = 0

# max_apareceu - rmazena a quantidade máxima de vezes que uma letra apareceu na frase até o momento.
max_apareceu = 0

# letra_max_apareceu - Armazena a letra que apareceu o maior número de vezes até o momento.
letra_max_apareceu = ''

while indice < len(frase):
    letra_atual = frase[indice]

# Se o caractere atual (letra_atual) for um espaço, o laço ignora e 
# continua para o próximo caractere. Isso é feito para evitar considerar espaços na contagem.
    if letra_atual == ' ':
        indice += 1
        continue

# A função count é usada para contar quantas vezes a letra_atual aparece na frase.
    qtd_apareceu_atual = frase.count(letra_atual)

# Se a quantidade atual de ocorrências da letra (qtd_apareceu_atual) for maior que 
# a quantidade máxima registrada até agora (max_apareceu),
# as variáveis max_apareceu e letra_max_apareceu são atualizadas com os novos valores.
    if max_apareceu < qtd_apareceu_atual:
        max_apareceu = qtd_apareceu_atual
        letra_max_apareceu = letra_atual

# O indice é incrementado para passar ao próximo caractere da string.
    indice += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_max_apareceu}" que apareceu '
    f'{max_apareceu}x'
)