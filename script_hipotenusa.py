#!/usr/bin/env python3
import sys

X = sys.argv[1] # pega o valor de X
Y = sys.argv[2] # pega o valor de Y


if str.isdigit(X) == True: # condicional para averiguar se as entradas são numeros 
	if str.isdigit(Y) == True:
		X = int(X) # transforma X em int
		Y = int(Y) # transforma Y em int
	else:
		print('digite dois numeros')
else:
	print('digite dois numeros')

Z = X^2 + Y^2  # armazena o valor do quadrado da hipotenuza em Z

print('O quadrado da hipotenusa para o triangulo com lados a=',X,'e b=',Y,' é',Z)
