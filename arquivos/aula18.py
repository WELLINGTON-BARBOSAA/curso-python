"""Aula sobre como funciona o Debugger.
Sua função serve para aprender como esta funcionando seu codigo de cima para baixo da esquerda para direita, o fluxo. 
Ele primeiro faz a leitura das condições existente no codigo.
Depois de fazer a leitura das condições o Debugger vai executar o primeiro IF e suas 
condições até achar a verdadeira, ao encontrar a mesma ele não tem mais o que executar 
e vai para o proximo IF. Se caso ele não encontrar nenhuma condição verdadeira o Debugger
vai passando até o outro IF existente no codigo"""


condição1 = False
condição2 = False
condição3 = False
condição4 = False
condição5 = True

if condição1:
    print("Condição 1 é falsa")

elif condição2:
    print("Condição 2 é falsa")

elif condição3:
    print("Condição 3 é verdadeira")

elif condição4:
    print("Condição 4 é falsa")

elif condição5:
    print("Esta condição é Verdadeira")

else:
    print("nenhuma das condições foram executadas")
    print("Sair dos sistema")

if 10 == 10:
    print("outro if")

print("Fora do if")