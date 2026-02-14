from sys import path

import aula99_package.modulo #1
from aula99_package import modulo #2
from aula99_package.modulo import * # O all só funciona se for importado tudo --> * <--
# não é uma boa pratica de programação
# print(*path, sep='\n') # esse comando me mostra a pasta main do arquivo - /home/wellington/Área de Trabalho/curso_Python/arquivos

print(soma_modulo(1,2)) 
print(aula99_package.modulo.soma_modulo(1,2)) 
print(modulo.soma_modulo(1,2)) 

print(variavel)