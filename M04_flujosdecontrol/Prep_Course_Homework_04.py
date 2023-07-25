#!/usr/bin/env python
# coding: utf-8
# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

numInt = 0

if(numInt>0):
    print("Es mayor a cero")
elif(numInt==0):
    print("Es igual a cero")
else:
    print("Es menor a cero")



# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

var1 = 5
var2 = 2
if(type(var1) == type(var2)):
    print("Son del mismo tipo")
else:
    print("Son de diferentes tipos")


# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
i = 1
while(i <=20):
    if(i % 2 == 0):
        print("El número ", i, " es par")
        i+=1
    else:
        print("El número ", i, " es impar")
        i+=1




# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
values = [0, 1, 2, 3, 4, 5]

for e in values:
    print("Para el valor",e, ".El resultado es", e**3)


# 5) Crear una variable que contenga un número entero
#    Realizar un ciclo for la misma cantidad de ciclos

# In[10]:
numInt = 6

for num in range(1, numInt):
    print("Ciclo numero",num)



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable
#    Sólo si la variable contiene un número entero mayor a 0

# In[33]:
varNum = 5
result = 0

if(type(varNum) == int):
    while(varNum > 0):
        if(result == 0):
            result += varNum * (varNum - 1)
            varNum -= 1
        elif(varNum != 1):
            result = result * (varNum - 1)
            varNum -= 1
        else:
            varNum -= 1
        print("Current result:",result)
        print("Cicles amount:",varNum)
elif(varNum == 0):
    print("The number is equal to zero")
else:
    print("The number is smallest to zero")

print("Factorial:", result)

# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
x = True
list = [1, 2, 3, 4, 5]

while(x == True):

    for e in list:
            print(e)
    break

# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

for n in list:
    while(n):
        print(n)
        break


# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

amountNumber = 30
n = 0 
primo = True

while(n < amountNumber):
    for division in range(2, n):
        if(n % division == 0):
            primo = False
    if(primo):
        print(n)
    else:
        primo = True
    n += 1

# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

while(n < amountNumber):
    for div in range(2,n):
        if(n % div == 0):
            primo = False
            break
    if(primo):
        print(n)
    else: 
        primo = True
    n+=1




# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:
cantidad_de_ciclos = 0
amountNumber = 30
n = 0 
primo = True

while(n < amountNumber):
    for division in range(2, n):
        cantidad_de_ciclos += 1
        if(n % division == 0):
            primo = False
    if(primo):
        print(n)
    else:
        primo = True
    n += 1

print("Cantidad de ciclos: " + str(cantidad_de_ciclos))

# In[57]:

amountNumber = 30
cantidad_de_ciclos = 0
primo = True
n = 0 

while(n < amountNumber):
    for div in range(2, n):
        cantidad_de_ciclos += 1
        if(n%div==0):
            primo=False
            break
    if(primo):
        print(n)
    else:
        primo=True
    n += 1

print("Cantidad de ciclos: " + str(cantidad_de_ciclos))


# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

# In[58]:

amountNumber = 100
cantidad_de_ciclos = 0
primo = True
n = 0 

while(n < amountNumber):
    for div in range(2, n):
        cantidad_de_ciclos += 1
        if(n%div==0):
            primo=False
    if(primo):
        print(n)
    else:
        primo=True
    n += 1

print("Cantidad de ciclos: " + str(cantidad_de_ciclos))



# In[59]:

amountNumber = 100
cantidad_de_ciclos = 0
primo = True
n = 0 

while(n < amountNumber):
    for div in range(2, n):
        cantidad_de_ciclos += 1
        if(n%div==0):
            primo=False
            break
    if(primo):
        print(n)
    else:
        primo=True
    n += 1

print("Cantidad de ciclos: " + str(cantidad_de_ciclos))


# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

inicio = 99
tope = 300
ciclos = 0

while(inicio <= tope):
    ciclos += 1
    inicio += 1
    if(inicio%12!=0):
        continue
    print(inicio)

print("Ciclos: " + str(ciclos))

# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:

n = 1
sigue = 1
primo = True
while (sigue == 1):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
        print('¿Desea encontrar el siguiente número primo?')
        if (input() != '1'):
            print('Se finaliza el proceso')
            break
    else:
        primo = True
    n += 1
        
# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

4# In[75]:

n = 100
while(n<=300):
    if (n % 3 == 0 | n % 6 == 0):
        print('El número es: ', str(n))
        break
    n += 1



# %%
