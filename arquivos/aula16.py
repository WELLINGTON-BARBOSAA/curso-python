# if / elif     /else
# se / se não se/ se não

entrada = input('Voce deseja "entrar" ou "sair" do sistema?: ')

if entrada == "entrar":
    print("Você entrou no sistema, aguarde enquanto o sitema esta sendo inicializado")

elif entrada == "sair":
    print("Voce saiu do sistema, aguarde enquanto o sistema esta sendo encerrado")

else:
    print("Você ainda não digitou nada até o momento ")