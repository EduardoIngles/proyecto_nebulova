# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 21:03:56 2021

@author: eduar
"""

#math

#Ejercicio 1

import math
    
a=[1,2,3,4]
b=[3,5,7,8]
c= [a]+[b]

for i in range (1,2):
    for n in range(len(i)):
        c= math.pow(i[n],2)
    
    
    
    
a= c[:(int(len(c)/2))]
a


lista1= [1,2,3,4]
lista2=[5,6,7,8]
matriz = [lista1,lista2]
matrizaca= "buenas tartes"

         
for i in range(len(matriz)): 

    fila = matriz[i] 

    for j in range(len(fila)): 
        matriz[i][j]=matriz[i][j]*2
matriz

#EJERCICIO 2


lista1= [1,2,3,4]
lista2=[5,6,7,8]
matriz = [lista1,lista2]
matriz

         
for i in range(len(matriz)): 

    fila = matriz[i] 

    for j in range(len(fila)): 
        matriz[i][j]=math.log1p(matriz[i][j])
lista1=matriz[0]
lista2=matriz[1]
print(lista1)
print(lista2)

math.log(2, 2)


#EJERCICIO 3

import math

vector1= [1,2]
vector2=[5,6]
suma = 0
for n in range(len(vector1)): 
   suma += (vector2[n]-vector1[n])**2
suma
suma=math.sqrt(suma)
suma

#EJERCICIO 3Crea una sucesión de números entre [0, 2\pi) con incremento de 0.01
# y guarda los elementos en una lista (debes utilizar un while).  


lista=[0,50]
a = 0
while a < ((lista[-1])-1):
    a+=1
    lista.insert(-1,a)
lista



len(set1)
set1[1]
set1=("hola buenas tardes")
set2={"Estoy en casa"}
coinciden =0
nocoinciden =0

for n in range len(set1):
    
import math


 hola = [0, ]

#EJERCICIO 5

print(f"{coinciden=}")
yield








