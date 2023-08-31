#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 14:21:23 2022

@author: nicmn
"""
#%% DEFININDO UM DICIONÁRIO:

d = {}
d = dict()
print(d, type(d))

#%% MODO 1:
# As chaves precisam ser únicas, os valores não precisam ser

d1 = {'ano':2001, 'mês':'Janeiro', 'dia':20, 40:50.5, 4+3j: [1, 2, 3]}
print(d1, type(d1))

print()

#EXERCÍCIO:
d = {0: 91.3,
     -16.55: None,
     'Júpiter': 'Europa',
     -2+3j: [1, 2, 3], 
     'orange':(-7, 'Py', 2.3),
     (5, 17): 25}

print(d)
print(d[0])
print(d[5, 17])

#%% MODO 2: quando todas as chaves são strings

d2 = dict(ano=2022, mês='Agosto', dia=17)
print(d2)
print(d2['mês'])

#%% MODO 3: lista de tuplas

d3 = dict([ ('ano', 2022), ('mês', 'Agosto'), ('dia', 17)] )
print(d3)
print(d3['dia'])

#%% MODO 4: usando a função zip()
# atribui valor para cada 
t1 = ('ano', 'mês', 'dia')
t2 = (2022, 'Agosto', 17)

print( zip(t1, t2)) #zip: coleção de dados 

for e in zip(t1, t2):
    print(e)
    
d4 = dict( zip(t1, t2))
print(d4)

#%% MODO 5:
# fromkeys: atribui um valor igual para todas chaves{}, 

d = {}.fromkeys(['ano','mês','dia']) # como não possui retorna None
print(d)

print()

d = {}.fromkeys(['ano','mês','dia'], 0)
print(d)

print()

da = d.fromkeys(['a', 'b', 'c'], -1)
print(da)
#%% EXEMPLO:

estrela = dict(
         Nome= 'Sirius',
         AR= '10:40:51',
         DEC= '-30:20:11',
         Mag= -1.2)

print(estrela['Mag'])

#%%

d = {1:10, 2:20, 3:30, 3:31, 3:32, 4:40, 5:50} 
print(d) # substituiu com o último valor escrito da chave 3

del d[5]
print(d)

#%% MÉTODOS

d1 = d.copy() #copiando um dicionário
print(d, d1, end='\n\n')

d1.clear() #d1 se tornou dicionário vazio
print(d, d1, end='\n\n') 

d1 = d.copy()
e = d1.pop(2) #retorna o valor do item e remove do dicionário o item
print(d, d1, e, end='\n\n')

x = d1.pop('abc', 'Item inexistente')
print(d, d1, x, end='\n\n')

d1 = d.copy()
print(d1)
x = d1.popitem()
print(d, d1, x, end='\n\n')

print(d[4])
print(d.get(4))

#print(d['abc']) #ERRO
print(d.get('abc'))

print(d.items())

print()

for i in d.items():
    print(i)
    
print()

for i in d:
    print(i)
    
print()

for k in d.keys():
    print(k)
    
print(d.keys())

print()

for v in d.values():
    print(v)
    
d.setdefault(5, 50)
print(d)

d.setdefault(6)
print(d)

dnew = {7:70, 8:80, 'nove':90}
print(dnew)

d.update(dnew)
print(d)
    
#%% VISUALIZAÇÃO:

print(d)
print(d.items)
print(d.keys)
print(d.values)  

print(d)
print(d.items())
print(d.keys())
print(d.values())

#%% OPERAÇÕES ENTRE CONJUNTOS 

a  = {1:10, 2:20, 3:31, 4:41}
b =  {3:32, 4:42, 5:50, 6:60}
print(a,b)

print(a.items() & b.items() ) #intersecção
print()

print(a.items() | b.items() ) #união
print()   

print(dict(b.items() | a.items()) ) #CONVERTENDO PRA DICT - união
print()

print(a.items() - b.items() ) #diferença
print()  

print(a.items() ^ b.items() ) #diferença simétrica
print() 
    
#%% COMPRESSÃO DE DICIONÁRIOS:

d = {k:k**2 for k in range(1, 6)} #conjunto semiaberto à direita
print(d)    

d_inv = {v:k for k,v in d.items()} #invertendo 
print(d_inv)  

#%% EXEMPLO:

import os #sistema operacional
dirx = '/home/nicmn/'
lista = os.listdir(dirx)
print(lista)

dsys = { nome : os.path.getsize(dirx + nome) for nome in lista} 

#print(dsys) #dsys: dicionário do sistema

for file, size in dsys.items():
    print("{0:20} {1:10} ".format(file,size))    
   
    
    
    
    
    
    
    
    
    
    
    
    













