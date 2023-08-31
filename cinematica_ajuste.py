#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   
	DESCRIÇÃO:
		Ajustando dados sintéticos gerados com numpy para, assim, 
        analisar a cinemática de uma partícula.  
        
        x = x0 + v0 * t + 1/2 * a * t
        
        O modelo será aceitável quando for maior que zero e constante.
        
	AUTOR:
		N. M. Narvaz
		00318736@ufrgs.br
	 
	VERSÃO:
	0.01 - 03.10.2022
"""

import numpy as np
import matplotlib.pyplot as plt
MODE_TEST = True

#Lendo dados:
data_dir = '/home/nicmn/prog/python/FIS02213/cinematica/dados/'

file_data = "simulacao1.dat"

if not MODE_TEST:
    file_data = input("Arquivo com dados: ")
    
file_data = data_dir + file_data

dados = np.loadtxt(file_data)

#Extraindo dados:
T = dados[0]
X = dados[1]

#Ajustando o modelo matemático:
coef = np.polyfit(T, X, 2) # coeficiente ordem 2
x0 = coef[2]
v0 = coef[1]
a = 2 * coef[0]
predict = np.poly1d(coef) #objeto do tipo function
Var = np.sum( (X - predict(T))**2 )/(X.size - 3) 

coef1 = np.polyfit(T, X, 1)
c0 = coef1[1]
c1 = coef1[0]
predict1 = np.poly1d(coef1)
Var1 = np.sum( (X - predict1(T))**2 )/(X.size - 2) 

t = np.linspace(min(T), max(T), 100) # valor mínimo e máximo de T
x = x0 + v0 * t + 0.5 * a * t**2
x1 = c0 + c1 * t

print(f" Posição inicial (m) ........x0 = {x0:5.2f}") # 5 casas pós vírgula e    
print(f" Velocidade inicial (m/2) ...v0 = {v0:5.2f}") # 2 dígitos
print(f" Aceleração (m/s**2) .........a = {a:5.2f}")

#Plotando:
plt.scatter(T, X) # <<<<<< dados
plt.plot(t, x, c="black", label = "modelo: x(t) = x0+v0*t+0.5*a*t^2")
plt.plot(t, x1, c="red", label = "modelo: x(6) = x0+v0*t")
plt.legend(loc="best")
plt.title("Movimento da partícula")
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")






