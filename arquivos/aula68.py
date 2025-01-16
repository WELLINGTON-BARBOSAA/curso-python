''' Escopo de funções em Python
Escopo significa o local onde aquele codigo vai atingir.
Existe o escopo global e local. 
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados '''

x = 5 # Esse x esta no escopo global 
# Pode definir uma variavel antes da função ser executada
# mas não depois da execução 
def escopo ():
    global x
    x = 10 # Esse x esta no escopo local
    def outro_escopo():
        global x
        x = 11
        y = 10

        print(x,y)
    outro_escopo() # parentese executa função

    print(x)
print(x)
escopo()
print(x)


# x = 1
# y = 2 

# def escopo ():
#     x = 4
#     def outro_escopo():
#         print(x)

#     outro_escopo()

# escopo()
# print(x)
# print(y)
# print(x,y)

    