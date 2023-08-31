#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:28:48 2022

@author: nicmn
"""

def Bhaskara(a, b, c):
    
    '''Retorna as raízes de uma equação de segundo grau
    do tipo: 
        a*x**2 + b*x + c = 0'''
        
    from cmath import sqrt
    
    # Entra as raízes usando Bhaskara:
    delta = b**2 - 4 * a * c
    
    x1 = -b/(2*a) - sqrt(delta)/(2*a)
    x2 = -b/(2*a) + sqrt(delta)/(2*a)
    
    # se as raízes forem reais, pega a parte real:
    if delta >= 0:
    	x1 = x1.real
    	x2 = x2.real
    
    # Identifica o número e o tipo de raiz:
    if delta > 0:
    	mens = "duas raízes reais"
    else:
    	if delta == 0:
    		mens = "uma raiz real"
    	else:
    		mens = "duas raízes complexas"

    return (x1, x2, mens, delta)
#%%
    
def somatorio(*x):
    ''' Retorna o somatório de uma sequência de valores. '''
    if len(x) == 0:
        raise ValueError("Lista vazia de valores.")
        
    soma = 0
    
    for e in x:
        if type(e) not in (int, float):
            raise TypeError("Valor não numérico.")
        soma += e
    return soma
#%%

def media(*x):
    ''' Retorna a média de uma sequência de valores. '''
    try:
        soma = somatorio(*x)
    except ValueError:
        raise ValueError("Lista vazia de valores.")
    except TypeError:
        raise TypeError("Valor não numérico.")
        
    n = len(x)
    mediax = soma/n
    return mediax
#%%
    
def variancia(*x):
    ''' Retorna variância de uma sequência de valores.'''
    
    n = len(x)
    
    if n < 2:
        raise ValueError("Menos do que 2 valores.")
    
    try:    
        xmedia = media(*x)
    except TypeError:
        raise TypeError("Valor não numérico.")
    
    soma = 0
    for e in x:
        soma = (e - xmedia)**2
        
    var = soma/(n-1)
    
    return var
#%%
 
def desvio_padrao(*x):
    
    from math import sqrt
    
    return sqrt(variancia(*x))















    