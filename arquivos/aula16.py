# if / elif     /else
# se / se não se/ se não

entrada = input ("Voce deseja 'entrar' ou 'sair' do sistema? " )

if entrada == 'entrar':
    print("voce entrou no sistema")
    print("Por gentileza, aguarde enquanto o sistema esta sendo inicializado")
elif entrada == 'sair':
    print("Voce digitou sair do sistema")
    print("Por favor, aguarde enquanto o sistema é encerrado")
else:
    print("Voce não digitou nada até o momento")