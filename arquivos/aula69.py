"""Escopo de funções em Python
Escopo significa o local onde aquele codigo pode atingir
Existe o escopo global e local
O escopo global é o escopo onde todo o código é alcançavel. 
O escopo local é o escopo onde apenas nomes do mesmo local
pode ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos
A palavra Global faz uma variavel de escopo externo 
ser a mesma mesma do no escopo interno""" 

# Se o x interno nãp tiver valor, o programa vai procurar nos escopos externos
# até achar, mas se caso não achar dá erro e pede para definir um valor para x.
# A execução da função tem que existir na mesma linha
x = 1
y = 5

def escopo_1():
    x = 2
    y = 3
    print(x,y)
    def escopo_2():
        x = 12
        y = 82
        print(x,y)
        def escopo_3():
            x = 58
            y = 4
            z = 15
            print(x,y,z)
            def escopo_4():
                x = 20
                y = 50 
                z = 23
                print(x,y,z)
            escopo_4()
        escopo_3()
    escopo_2()

escopo_1()
print(x,y)
