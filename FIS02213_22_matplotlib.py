#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	MATPLOTLIB - Biblioteca gráfica do Python

	AUTOR:
		N. M. Narvaz / @author: nicmn
		00318736@ufrgs.br
	
	REFERÊNCIAS: 
		https://matplotlib.org/stable/tutorials/index.html
        https://www.rapidtables.com/web/color/RGB_Color.html
        ps://www.geeksforgeeks.org/matplotlib-pyplot-annotate-in-python/
	BUGS/LIMITAÇÕES:

	ToDos:
		<alterações/correções a fazer>
	
	OBSERVAÇÕES:
		Para tornar executável:
		% chmod ugo+x <nome_do_programa>
		
		Para criar um link em ~/bin:
		% ln ~/prog/python/programa.py> ~/bin/<programa>
	 
	VERSÃO:
	0.01 - 24/08/2022
"""
#%% IMPORTANDO MÓDULOS:

import matplotlib.pyplot as plt
from math import pi, sin, cos, tan, log10
#%%
x = [-pi + e*0.01 for e in range(0, int(2*pi/0.01))]
print(x)
print()

xrange = lambda x1, x2, dx: [x1 + e*dx for e in range(0, int((x2 - x1)/dx))]
print(xrange(-pi, pi, 0.01))

#%%
n = xrange(-pi, pi, 0.01)
y1 = [sin(n) for n in x]
y2 = [cos(n) for n in x]
y3 = [log10(abs(tan(n)))*0.1 for n in x]
y4 = [log10(1/n**2) for n in x]

xdata = [-2, -1.7, 0.7, 1.8, 2.8]
ydata1 = [-1.1, -1.5, 0.4, 1.5, 0.7]
ydata2 = [-1*x for x in ydata1]
ydata3 = [x**2 for x in ydata1]

plt.plot(x, y1, 'b-', label = "sin(x)")              #SÓLIDA
plt.plot(x, y2, 'c--', label = "cos(x)")             #TRACEJADA
plt.plot(x, y3, 'm:', label = "log10(tan(1/n^2))")  #PONTILHADA
plt.plot(x, y4, 'y-.', label = "log10(1/n^2)")       # -.

#CORES: b: blue, c: cyan, m: magenta, y: yellow / lw: largura do traço.

plt.title("Gráfico 1 <3")
plt.xlabel("x")
plt.ylabel("y")

plt.plot(xdata, ydata1, 'ro', label = 'ydata1')
plt.plot(xdata, ydata2, 'b*', label = 'ydata2')
plt.plot(xdata, ydata3, 'ks', label = 'ydata3')
plt.grid(True, linestyle='--')

plt.legend(loc = 1)
#loc: localização das legendas
#0: best; 1:SD; 2:SE; 3:IE; 4:ID; 5:D; 6:CE; 7:CD; 8:IC, 9:SC; 10:C.

#%% DIAGRAMAS DE DISPERSÃO:
import random

x = [random.gauss(0, 1) for k in range(0, 100)]
y = [random.gauss(0, 1) for k in range(0, 100)]

plt.scatter(x,y)
plt.title("Diagrama de dispersão")
plt.xlabel('x')
plt.ylabel('y')

#%% DIAGRAMAS DE BARRAS:

tipos = ['O', 'B', 'A', 'F', 'G', 'K', 'M']
numero = [10, 11, 8, 19, 23, 35, 30]
cores = ['red', 'blue', 'magenta', 'green', 
         'orange', 'cyan', 'yellow']

plt.bar(tipos, numero, color=cores)

#%% DIAGRAMA DE PIZZA:

explosao = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
             
plt.pie(numero,
        labels = tipos,
        autopct = "%4.1f%%", #%: formato, f: float, %%: %
        shadow = True,      #shadow deixa uma sombrinha como se fosse 3d
        startangle = 90,    #gira em 90 graus
        explode = explosao) #separa os espaços da pizza

#%% HISTOGRAMAS PARA VARIÁVEIS CONTÍNUAS:
import random 
from math import sqrt

massas = [random.gauss(1,0.2) for i in range(0, 1000)]
plt.hist(massas, 
         density=True, 
         bins=int(sqrt(1000)),
         color='pink')

#%% MÚLTIPLOS GRÁFICOS EM UMA FIGURA:

x = [e/100 for e in range(-100, +100)]
y1 = [e**2 for e in x]
y2 = [e**3 for e in x]
y3 = [cos(e) for e in x]
y4 = [sin(e) for e in x]

plt.figure(figsize = (8, 6))

#numero de linhas, colunas e gráficos
plt.subplot(2, 2, 1) 
plt.plot(x, y1)
plt.title("Gráfico 1")
plt.xlabel('x')
plt.ylabel('y1')

plt.subplot(2, 2, 2) 
plt.plot(x, y2)
plt.title("Gráfico 2")
plt.xlabel('x')
plt.ylabel('y2')

plt.subplot(2, 2, 3) 
plt.plot(x, y3)
plt.title("Gráfico 3")
plt.xlabel('x')
plt.ylabel('y3')

plt.subplot(2, 2, 4) 
plt.plot(x, y4)
plt.title("Gráfico 4")
plt.xlabel('x')
plt.ylabel('y4')

#AJUSTES
plt.subplots_adjust(
        top = 0.92, 
        bottom = 0.08, 
        left = 0.10, 
        right = 0.90, 
        hspace = 0.55, 
        wspace = 0.5
        )

#%% LIMITES DOS EIXOS:

#Exemplo 1:
plt.plot(x, y1)
plt.title("Gráfico 1")
plt.xlabel('x')
plt.ylabel('y1')

plt.xlim(-0.5 , +0.5)
plt.ylim(0, 0.3)

plt.text(-0.2, 0.25, "Aquiii")
plt.text(-0.2, 0.20, "$\\alpha=3.35$")
plt.text(-0.35, 0.25, "$\\beta=\\frac{a}{b}$")

plt.annotate("Observação", 
             xy=(-0.3, 0.09),
             xytext=(-0.2, 0.06),
             arrowprops=dict(facecolor='black', shrink=0.2))

#%% GRÁFICOS LOGARÍTMICOS:

x = [e for e in range(1, +100)]
y = [log10(e) for e in x]

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')

plt.xscale('linear') 
plt.yscale('log') #escala em logarítimica

#%% COORDENADAS POLARES:

from math import sin, radians

# Figura bonita kkk
#theta = [e for e in range(0, 360)]
#r = [e/360 for e in theta]

#plt.polar(theta, r)

theta = [radians(e) for e in range(0, 360)]
r = [e for e in theta]

plt.polar(theta, r)



























