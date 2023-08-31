#!/usr/bin/env python3

# Resolve uma equação de 2o. grau, do tipo:
# a*x**2 +b*x + c = 0 
# encontrando suas raízes.
# 
# AUTOR:
# 	N. M. Narvaz
# 	00318736@ufrgs.br
#
# OBSERVAÇÕES: 
# 	Para tornar executável:
#		% chmod ugo+x FIS02213_08_bhaskara.py
# 
#		Para criar um link em ~/bin:
#		% ln ~/prog/python/FIS02213_08_bhaskara.py ~/bin/bhaskara
#
# Bugs/ Limitações: 
# * uma exceção é lançada (ocorre um erro) quando um dos valores
#   de a, b ou c não tem a sintaxe de um número inteiro, float
#   ou complex.
#
#  VERSÃO:
#	0.01 - 06/07/2022
#   0.02 - 27/07/2022
#   0.03 - 08/08/2022 (versão Spyder)

# Importando módulos:
import sys
import meumodulo

#%% FUNÇÃO PRINCIPAL

# Abertura 
barra = ' ' + 70*'-'
print()
print(barra)
print('''Resolve uma equação de 2o. grau do tipo:
         a*x**2 + b*x + c = 0
				 
				 Versão Spyder 0.03''')
print(barra)
print()

# Entra valores de a, b e c:
try:
	a = float( input("Digite o valor de a: ") )
	b = float( input("Digite o valor de b: ") )
	c = float( input("Digite o valor de c: ") )
 
except Exception:
	print("Digite um valor válido e tente novamente", end='\n\n')
	sys.exit()
 
x1, x2, mens, delta = meumodulo.Bhaskara(a ,b, c)


# Saída de dados:
print()
print(f" O discriminante da equação é: {delta}")
print(f" Esta equação tem {mens}")
print(f" A raíz x1 é igual a {x1}")
print(f" A raíz x2 é igual a {x2}")

print(barra, end='\n\n')
