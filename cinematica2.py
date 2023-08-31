#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	Gera dados sintéticos UTILIZANDO NUMPY 
   
	DESCRIÇÃO:
	Gerando dados sintéticos para analisar a cinemática de uma 
    partícula.  

	AUTOR:
		N. M. Narvaz / @author: %(username)s
		00318736@ufrgs.br

	VERSÃO:
	0.01 - %(date)s
"""

import numpy as np

data_dir = '/home/nicmn/prog/python/FIS02213/cinematica/dados/'

# Define os tempos:
t1 = float( input("Digite t1 (s): ")) #TODO: float
t2 = float( input("Digite t2 (s): ")) #TODO: t2>t1
n = int( input("Número de medidas: ")) #TODO: n>1

deltaT = (t2-t1)/(n-1) #TODO: n>1

T = np.linspace(t1, t2, n)

# Entra x0, v0, a
x0 = float( input("Digite x0 (m): "))
v0 = float( input("Digite v0 (m/s): "))
a  = float( input("Digite a (m/s2): "))

# Gerando as medidas das posições:
Xteorico = x0 + v0*T + 0.5*a*T**2

deltaX = np.random.normal(0, scale = 1.0, size = Xteorico.size)

Xmedido = Xteorico + deltaX

#Salvando os dados:
file_output = input("Digite o nome do arquivo: ")
file_output = data_dir + file_output #concatena os dois

dados = np.stack((T, Xmedido))

np.savetxt(file_output, dados) #, delimiter= ",")
#np.save(file_output, dados)
#np.savez_compressed(file_output, dados)