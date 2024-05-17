# Operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras
# Se qualquer valor for considera falso
# a expressão inteira será avaliada naquele Valor 
# São considedaros falsy (que eu ja vi)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para respresentar um não valor

entrada = input ("[E]ntrar ou [S]air: ")
senha_usuario = input ("Senha: ")
senha_permitida = '741Samsung'

if entrada == 'E' and senha_usuario == senha_permitida:
    print("Entrou no sistema, parabéns")

else:
    print("Saiu do sistema")




# print (True and True and False and True and True)
# # Avaliação de curto circuito
# # # Codigo só avança de acordo com o True, se achar um False o programa para exatamente no False
