#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 14:53:26 2022

@author: nicmn
"""
#%% CODE TAGS - sempre em letra maiúscula
# vá em Source > Show todo list

#TODO : coisas a se fazer.
#FIXME : funciona, melhora, caso particular de TODO.
#XXX : possíveis falhas.
#BUG : tem um problema!
#OPTMIZE : otimizar.
#!!! : alerta!
#??? : dúvida.
#HACK : parte do código não está bem escrita mas funciona.

#%%
import matplotlib.pyplot as plt
import math

def quadrado(x):
    """Retorna uma tupla com os quadrados de x"""
    y = []
    
    for elemento in x:
        b = elemento**2
        y.append (b)
        
    return tuple(y)


x = list(range(-10,10))
y = quadrado(x)

plt.plot(x,y)
