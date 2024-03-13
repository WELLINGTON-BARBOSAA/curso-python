# if / elif     /else
# se / se não se/ se não

entrada = input ("Voce deseja 'entrar' ou 'sair' do sistema?")

if entrada == "entrar":
    print("Voce acabou de entrar no sistema")
    print("Aguarde, enquanto o sistema esta carregando")

elif entrada == "sair":
    print("Voce acabou de sair do sistema")
    print("Aguarde, enquanto o sistema é encerrado")

else:
    print("Voce não digitou nada ate o momento")