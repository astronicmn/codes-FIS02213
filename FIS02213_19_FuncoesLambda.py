#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 13:43:18 2022

@author: nicmn
"""

from math import sqrt
#%% 

distancia = lambda  x, y: sqrt(x**2+y**2) #x e y parâmetros de entrada 
quadrado = lambda x: x**2 #retorna quadrado de x


x = 10
y = 10
print("Distância: ",  distancia(x, y)) 
print("Quadrado: ", quadrado(x))

#%% Funções lambda anônimas 

lambda x, y: x+y

#%%

lambda x: x**2 #função lambda que depende só de x

# _ (underline) CRIA FUNÇÃO ANÔNIMA 
# Exemplo: _(5) : 25

#%%
quadrado = lambda x: x**2
f = lambda x, y, func: sqrt(func(x) + func(y)) 
g = lambda x, y: sqrt(quadrado(x) + quadrado(y))

print("f: ", f(1, 2, quadrado))
print("g: ", g(1, 2))