# Operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras
# Se qualquer valor for considera falso
# a expressão inteira será avaliada naquele Valor 
# São considedaros falsy (que eu ja vi)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para respresentar um não valor

# ESTA AULA FALA SOBRE OR

entrada = input ("Para Entrar digite [E] e para sair digite [S]")
senha_usuario = input("Digite sua senha:")
senha_permitida = "7411"

if entrada == 'E' and entrada == 'e' or senha_usuario == senha_permitida:
    print("voce entrou no sistema")
else:
    print("Voce saiu do sistema")

# senha = input ("senha: ") or 'não digitou a senha'
# print(senha)


# # print(False or False or False or 'abc')

# #Acontece porque no or ele pula o os False até encontrar True