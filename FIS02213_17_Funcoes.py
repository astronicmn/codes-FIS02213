#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 14:02:11 2022

@author: nicmn
"""
                                                                               
#%% >> define novo bloco
# Definição de uma função com um único parâmetro.             
                                                   
def quadrado(x):
    """Retorna o quadrado de x."""
    return x**2  #comando que retorna para o código que chama função 
#%%
y = quadrado(5)
print(y)
#%%
# Definição de uma somba com mais de um parâmetro

def soma(a, b, c):  # parâmetros posicionais 
    '''Retorna a soma de a, b, c'''
    s = a+b+c
    return s 

print(soma (1, 2, 3)) 
#%% 
# Representação de uma função:

print(quadrado, type(quadrado))
print(soma)
#%%
# Argumentos com palavras chave

def divisao(a=1, b =0, c=1):
    '''Retorna a/b.'''
    return (a+b)/c

print(divisao(8, 4))
print(divisao(a=8, b=4))
print(divisao(b=4, a=8))
print(divisao(8, 4))
#print(divisao(a = 8,4)) # dá erro de sintaxe.

#%%
def potencia(x, n=1):
    return x**n

print(potencia(10))
print(potencia(10,3)) #10 elevado ao cubo

#%%
# Forçando o uso de argumentos com palavras chaves

def soma2(*, a, b, c):
    '''Retorna a soma de a, b, c.'''
    return a+b+c

print(soma2(a=10, b=20, c=30))

#%%
def soma3(a, *, b, c):
    '''Retorna a soma de a, b, c.'''
    return a+b+c

print(soma3(10, b=20, c=30))

#%% 
# Funções com um número arbitrário de parâmetros

def somatudo(*x):
    #print(type(x)) #tupla pois o processamento é mais rápido e imutável
    soma = 0
    for e in x:
        soma += e
    return soma

def media(*x):
    n = len(x)
    soma = somatudo(*x) # * (asterisco): função de desempacotamento de tupla.
    media = soma/n
    return media

print(somatudo(5))
print(somatudo(10, 20))
print(somatudo(10, 20, 30, 40, 50))        

print(media(10, 20, 30, 40, 50))


