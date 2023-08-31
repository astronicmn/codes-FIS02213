#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	Estudo sobre NumPy (Numerical Python).
   
	DESCRIÇÃO:
		<descrição + detalhada>

	AUTOR:
		N. M. Narvaz / @author: %(username)s
		00318736@ufrgs.br
	
	REFERÊNCIAS: 
		<[#] referência..>
	
	BUGS/LIMITAÇÕES:

	ToDos:
		<alterações/correções a fazer>
	
	OBSERVAÇÕES:
		Para tornar executável:
		% chmod ugo+x <nome_do_programa>
		
		Para criar um link em ~/bin:
		% ln ~/prog/python/programa.py> ~/bin/<programa>
	 
	VERSÃO:
	0.01 - 12/09/2022
"""

#%% IMPORTANDO MÓDULOS:
import numpy as np # p/ visualizar o que tem dentro -> dir(np)
import math as m
from math import sqrt, cos
import matplotlib.pyplot as plt
import random
import numpy.random as random #random versão numpy
#%% Arranjo com dimensão zero.
arr0d = np.array(10) 
print(arr0d, type(arr0d)) 

#%% ARRAY 1D - 1 arranjo unidimensional
lista = [x for x in range(1,13)]
arr1d = np.array(lista) #convertendo a lista para um array              
print(lista)
print(arr1d) 

#%% ARRAY 2D - 2 arranjos unidimensionais
arr2d = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
print(arr2d)

#%% ARRAY 3D - matriz com 2 sublistas
arr3d = np.array([ [[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]] ])
print(arr3d)
#%% ARRAY 4D - 2 subarranjos 3d
arr4d = np.array([arr3d, arr3d])
print(arr4d)

#%% PROPRIEDADES DOS OBJETOS ndarray:

# Número de elementos/ tamanho
print(arr0d.size) 
print(arr1d.size, len(arr1d))
print(arr2d.size)
print(arr3d.size)
print(arr4d.size, len(arr4d))

print()
# Número de dimensões
print(arr0d.ndim) 
print(arr1d.ndim) 
print(arr2d.ndim) 
print(arr3d.ndim) 
print(arr4d.ndim) 

print()
# Forma do arranjo
print(arr0d.shape) # tupla vazia
print(arr1d.shape) # tupla na primeira dimensão
print(arr2d.shape) # matriz de 2 linhas e 6 colunas
print(arr3d.shape) # 2 matrizes de 2 linhas e 3 colunas
print(arr4d.shape) # 2 arranjos 3d

#%% EXEMPLO:

arr = np.array([[[[[1, 2, 3, 4, 5]]]]])
print(arr.ndim, arr.shape)

print()
v = (1, 2, 3)
arr1d = np.array(v) #convertendo o vetor para array 1d
print(arr1d)

arr2d = np.array([arr1d]) #convertendo arr1d para array 2d
print(arr2d)

#%% ALTERANDO A FORMA DE UM ARRANJO:

arr1d = np.array(lista)
print(arr1d)
print(arr1d.shape)

print()
arr2d = arr1d.reshape(3, 4) # alterou a aparência em
                            # 3 linhas e 4 colunas
print(arr2d)

print()
arr2dm = arr1d.reshape(6, 2) # alterou a aparência em
                             # 6 linhas e 2 colunas
print(arr2dm)

print()
arr3d = arr2d.reshape(2, 3, 2) # tem de ser o mesmo número de elementos
print(arr3d)

print()
print(arr1d, '\n\n')
arr = arr1d.reshape(3, -1) # 
print(arr)

#%% ACESSANDO ELEMENTOS DE UM ARRAY:

print(arr1d)
print(arr1d[4])
print()

print(arr2d)
print(arr2d[1, 2]) # linha índice 1, coluna índice 2

#%% EXTRAINDO ELEMENTOS DE UM ARRANJO:

print(arr1d)
print(arr1d[2:8])
print()
#---------------------------------------------------------------------#
arr = arr1d.reshape(4, 3)
print(arr)
#--------------------------------------------------------------------#
a = arr[1:3, 1:]     # fatiamos o array do primeiro elemento até
                     # o segundo/começo fatiamento pela coluna 1
                     # até última coluna
print()
print(a)
print(type(a))
#--------------------------------------------------------------------#
print()
print(arr1d[::2]) # inicia e finaliza no primeiro e último elemento 
                  # indo de dois em dois

#%% ITERANDO UM ARRANJO:
                  
a = arr1d.reshape(3, 2, 2)
print(a)                  
print()

for x in a:
    #print("x =", x)
    for linha in x:
        #print("linha =", linha)
        for elemento in linha:
            print("elemento =", elemento)
    
print()
for x in np.nditer(a): #independente da forma 
    print("x =", x)

#%% FUNÇÕES UNIVERSAIS DO NUMPY:
    
x = np.array([x for x in range(-4,4)])
y = x**2
z = np.cos(x) #cosseno em função universal 

# comparando com matplotlib
plt.plot(x, y, color='indigo')
plt.plot(x, z, color='peru')

#%% FUNÇÕES PARA NÚMEROS RANDÔMICOS: 

print(random.randint(1, 100, size=10)) #numpy.random permite utilizar size
print()
print(random.randint(1, 100, size=(6,5)))
print()
print(random.rand(10)) 

x = random.normal(0, 1, size=1000) #média 0, desvio padrão 1
plt.hist(x, bins=30, color = 'salmon')

#%% GERANDO NDARRAYS:

a = np.array([1, 2, 3, 4])
print(a)

lista = [x for x in range(1, 11)]
print(lista)

a = np.arange(1, 11, 1)
print(a)

b = np.arange(0.3, 11.7, 0.1)
print(b)

c = np.linspace(-np.pi, +np.pi, 10) #10 valores
print(c)

#%% EXEMPLO:

x = np.linspace(-np.pi, +np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x + 0.5)
plt.plot(x, y1, color='black')
plt.plot(x, y2, color='magenta')

#%% GERANDO NDARRAYS COM 0s E 1s:

x = np.zeros(10)
print(x)

x = np.ones(5)
print(x)

#%% GERANDO NDARRAYS COM VALORES ALEATÓRIOS:

arr1 = np.random.rand(5)
print(arr1)
print()

arr2 = np.random.rand(5,2)
print(arr2)
print()

arr3 = np.random.random(3)
print(arr3)
print()

arr4 = -1 + 3 *np.random.random(10)
print(arr4)
print()

arr5 = np.random.randint(10, 20, 5)
print(arr5)
print()

arr6 = np.random.choice(np.arange(1, 20), 5, replace = False)
print(arr6)
print()

x = np.random.normal(10, 1, 1000)
plt.hist(x, bins = 50, color='teal')

x = np.random.uniform(-3, +5, 1000)
plt.hist(x, bins = 50, color='orchid')

#%% COPY & VIEW

a = np.arange(1, 13)
b = a.reshape(3, 4)
print(a, a.ndim, a.shape, end='\n\n')
print(b, b.ndim, b.shape)

print()
a[4] = 50
print(a)
print(b)

print()
a = np.arange(1, 13)
b = a.copy().reshape(3, 4)
print()

a[4] = 50
print(a)
print(b)

#%% ACHATAMENTO DE ARRAYS:

a = np.random.rand(3, 4)
print(a)
print()
print(a.flatten() )

#%% OPERAÇÕES:

# Escalares:
a = np.arange(1, 11)

print(a)
print(a + 10)
print(a - 5)
print(a * 2)
print(a / 3)
print(a**2)

# Binárias:
b = np.arange(21, 31)

print()
print(a)
print(b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a**b)

print()
c = np.random.random(a.size)
print(c)
print(a + np.cos(b)/c)

# Lógicas:
a = np.random.randint(-10, +10, 10)

print()
print(a)
print(a > 0)

#%% APLICANDO FILTROS:

a = np.random.randint(-10, +10, 10)
print(a)

filtro = a > 0
print(filtro)

print(a[filtro])

#%% EXEMPLO:

#1. Gerar arranjo de 1 a 100, 50 números inteiros.

x = np.random.randint(1, 100, 50)
print(x)

#2. Extrair todos valores em 30 a 40.

filtro = (x>=30) * (x<=40)
print(x[filtro])

'''
ou

filtro1 = x >= 30
filtro2 = x <= 40
print(x[filtro1 * filtro2])

'''
#%% CONCATENANDO ARRAYS 1D:
# sem vírgula arranjo(array), com vírgula lista

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print('\n', arr1, '\n', arr2, '\n')

print()
arr = np.concatenate((arr1, arr2))
print(arr)

#%% CONCATENANDO ARRAYS 2D:

arr1b = arr.copy().reshape(2, 3) # copiamos para não alterar array original
print(arr1b)

print()
arr2b = arr1b.copy() + 6 
print(arr2b)

print()
arr3 = np.concatenate((arr1b, arr2b), axis=0)
print(arr3)

print()
arr4 = np.concatenate((arr1b, arr2b), axis=1)
print(arr4)

print()

# Método .stack():
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
print( np.stack( (a1, a2), axis=1))
print()

print( np.hstack( (a1, a2))) #concatena horizontalmente
print( np.vstack( (a1, a2))) #verticalmente

#%% SEPARAÇÃO DE ARRAYS:

arr = np.arange(1, 7)
print(arr)

lista = np.array_split(arr, 3)
print(lista)
print(lista[0])

#
print()
lista2 = np.array_split(arr, 4)
print(lista2)

#
print()
b = np.arange(10, 20)
print(b)
print(np.array_split(b, 6))

#%% PESQUISAS EM ARRAYS:
# indo em variable explorer e clicando em value aparece tabela com valores

# Exemplo 1:
a = np.random.randint(1, 100, 50)

np.where(a==40)
#a==40 #contém valores booleanos, onde True retorna o índice

# Exemplo 2:
b = np.random.randint(1, 100, 100).reshape(10, 10)
print(b)

np.where(b==40)
print()

# Exemplo 3:
c = np.random.randint(1, 100, 10)
print(c)
print()
filtro = np.where(c%2==0) #divisão do arr c por 2 tem de ser 0

print(c[filtro])

#%% ORDENANDO ARRAYS: ordem crescente ou decrescente

e = np.random.randint(1, 100, 10)
print(np.sort(e))           #crescente
print(np.sort(e)[-1::-1])   #decrescente

#%% FUNÇÕES UNIVERSAIS:

print( type(m.cos))   # aceita 1 valor | <class 'builtin_function_or_method'>
print( type(np.cos))  # aceita 1 valor ou arranjo | <class 'numpy.ufunc'>
print()

x = 0.5
x1 = np.array(x)
y = np.array([0.5, 0.7, 0.8])

print(m.cos(x))
#print(m.cos(y)) # gera erro
print(m.cos(x1))

print()
print(np.cos(x))
print(np.cos(x1))
print(np.cos(y)) #retorna arranjos com cossenos dos respectivos valores de y

#%% CRIANDO UMA FUNÇÃO NORMAL:

#def distancia(p, q):
#    
#    ''' Retorna a distância entre o ponto p = (x1, y1)
#        e o ponto q = (x2, y2). '''
#        
#    x1 = p[0]; y1 = p[1]
#    x2 = q[0]; y2 = q[1]
#    d = sqrt((x2-x1)**2 + (y2-y1)**2)
#    return d     
#
#p = (5, 7)
#q = (-1, 3)        
#
#print("Distância: ", distancia(p,q))
#
#arrp = np.array([(1, 2), (3, 4), (5, 6)])
#arrq = np.array([(-1, -2), (-2, -3), (-3, -4)])
#
#udist = np.frompyfunc(distancia, 2, 1) #distância universal
#udist(arrp, arrq)

def cosseno(x):
    return cos(x)

print(cosseno(0.5))

a = np.array([0.1, 0.2, 0.3])
ucosseno = np.frompyfunc(cosseno, 1, 1) #função universal 
print('\n', ucosseno(a))

