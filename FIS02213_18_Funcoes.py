#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:17:54 2022

@author: nicmn
"""
# Importando módulos
import meumodulo
#%%
#
def soma(a, b, c):
    somatorio = a + b + c
    print(somatorio)
    return somatorio

a = 10
b = 20
c = 30
somatorio = a + b + c + 100
somatorio2 = soma(a, b, c)

print(somatorio, somatorio2)

#%%
# Função que soma sempre + 1 e contando...
cont = 10

def contador():
    global cont # permite que tu consiga acessar e alterar o valor
                # de uma variável que foi definida anteriormente
    cont += 1
    
    print(cont)
    
contador()
contador()
contador()
print(cont)

#%%
# Definindo variável e utilizando def show()
x = 111

def showx(x):
    #global x
    a = x**2
    print(a)
    print(locals()) # mostra variáveis locais 
    
showx(x) # código chamador 

#%%
x = 111

def showx(x):
    print(x)

print(a)
#%%
t = [10, 20, 30, 40, 50, 60]

print(meumodulo.somatorio(*t))  # SOMATÓRIO
print(meumodulo.media(*t))  # MÉDIA 
print(meumodulo.variancia(*t)) #VARIÂNCIA
print(meumodulo.desvio_padrao(*t))  #DESVIO PADRÃO

























