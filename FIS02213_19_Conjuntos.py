#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 14:12:35 2022

@author: nicmn
"""

#%% CRIANDO UM CONJUNTO:
#nos conjuntos os elementos não são indexados

s = {0, 10, 20, 30, 40}
print(f"conjunto s=(s)")

#%% CONJUNTO VAZIO:

s_vazio = {}
s2_vazio = set() #SET() cria um conjunto

print(s_vazio)
print(s2_vazio)

#%% CONVERTENDO PARA CONJUNTO:

L = {1, 2, 3, 4} #LISTA 
t = {10, 20, 30, 40} #TUPLA
string = "abcdef" 

print(set(L))
print(set(t))
print(set(string))

print(set(1)) #ocorre uma exceção pois não é iterável 

#%% TAMANHO DE UM CONJUNTO:

s = set(string)
print(s, len(s))

#%% UNICIDADE DE ELEMENTOS:

L = [10, 10, 10, 20, 20, 30, 30, 5, 5] #lista identa com colchetes
s = set(L)
print(L, "\n", s)

texto = 'Nulla vitae nulla ex.'
texto = texto.lower() # retorna texto com as letras maiúsculas como minúsculas
                      # em ordem alfabética (maneira classificada)
print()
print(texto)
s = set(texto) #convertendo texto para conjunto.

print()
print(s)
print()

alfabeto = set("abcdefghijklmnopqrstuvwxyz")
s = s & alfabeto

lista = list(s)
print(sorted(lista)) # SORTED classifica qualquer sequência (lista, tupla)
                     # e sempre retorna uma lista com os elementos de maneira 
                     # classificada, sem modificar a sequência original. 
                     
#%% OPERAÇÕES ENVOLVENDO CONJUNTOS:

s = {1, 2, 3, 4}
t = {3, 4, 5, 6}

uniao = s | t #une os elementos 
print(uniao) 

interseccao = s & t #comum aos dois conjuntos
print(interseccao) 

diferenca = s - t #elementos que estão em s e não em t 
print(diferenca)

print(t - s) #elementos que estão em t e não em s

diferenca_simetrica = s^t #oposto da intersecção
print(diferenca_simetrica)

#%% OUTRA MANEIRA:

s = {1, 2, 3, 4}
t = {3, 4, 5, 6}

print(s|t, s.union(t))
print()
print(s&t, s.intersection(t))
print()
print(s-t, s.difference(t))
print()
print(s^t, s.symmetric_difference(t))
print()
print(s.difference_update(t))

#%% EXEMPLO:
n = {10, 20, 30, 40}

n = {10, 20, 30, 40}
i = {50, 60, 70, 80}

print(n|i)
print(n&i)
print(n-i, i-n)
print(n^i) #nesse caso particular a união é igual a diferença simétrica 

#%% COMPRESSÃO DE CONJUNTOS:

lista = ['file' + str(i) + '.dat' for i in range(1, 7)] 
#concatena arquivo com um número (que varia de 1 até 6 + extensão .dat
print(lista)

print()

s = {'file' + str(i) + '.dat' for i in range(1, 7)}

print(s)

#%% MÉTODOS DE CONJUNTOS:
#conjuntos aceitam qualquer tipo de dado

s = {0, 10, 20, 30, 40, 'abc', 12.45}
print(s)

s.add(50) #adicionando um elemento ao conjunto
print(s)

s.update({'a','b','c'}) #conjunto de dados para ser adicionado ao conjunto
s.update([100, 200, 200, 300]) #dados repetidos são ignorados 
#s.update(70) #dá erro pois não é uma coleção de dados
print(s)

#%% MÉTODOS PARA REMOVER ELEMENTOS:

s = {1, 2, 3, 4, 5}

s.discard(3)
s.discard(6) #não existe o elemento mas a função discard é flexível
print(s)

s.remove(1)
#s.remove(6) #já o remove gera uma exceção/erro
print(s)
print()

s = {1, 2, 3, 4, 5}
print(s)
e1 = s.pop(); print(s, e1) #pop() remove elemento qualquer de um conjunto
e2 = s.pop(); print(s, e2)
e3 = s.pop(); print(s, e3)
e4 = s.pop(); print(s, e4)
e5 = s.pop(); print(s, e5)
#s.pop(); print(s) # gera erro por ser um conjunto vazio

print()
s = {1, 2, 3, 4, 5}
print(s)
s.clear() #limpa o conjunto 
print(s)

print()
s = {1, 2, 3, 4, 5}
e = s.pop(); s.add(e) # e: elemento / recoloca o elemento no conjunto 
print(s, e)
e = s.pop(); s.add(e); print(s, e)
e = s.pop(); s.add(e); print(s, e)
e = s.pop(); s.add(e); print(s, e)
e = s.pop(); s.add(e); print(s, e)
e = s.pop(); s.add(e); print(s, e)

#%% COPIANDO CONJUNTOS:

s = {1, 2, 3, 4, 5}
t = s

print(s, t)

t.discard(5)
print(s, t)

#%% COPIANDO CONJUNTOS PARTE 2:

s = {1, 2, 3, 4, 5}
t = s.copy() # t é um novo conjunto (cópia de s) podemos, aqui, alterar o 
             # conjunto t sem afetar o conjunto s.
           
t.discard(5)
print(s, t)

#%%
for elemento in s:
    print(elemento)









































