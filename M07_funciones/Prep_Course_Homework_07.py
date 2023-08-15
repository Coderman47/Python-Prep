#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro 
#    devuelva True si es primo o False si no lo es.

# In[1]:
def isPrimo(num):
    esPrimo=True
    for div in range(2, num):
        if(num % div == 0):
            esPrimo = False
            break
    if(num != 1):
        return esPrimo
    else:
        return False

isPrimo(1)

# 2) Utilizando la función del punto 1
#    Realizar otra función que reciba de parámetro una lista de números
#    Devolver en otra lista sólo aquellos que son primos

# In[25]:
def verifyPrimoInList(lista):
    primoList= []
    for number in lista:
        verifyPrimo = isPrimo(number)
        if(verifyPrimo == True):
            primoList.append(number)
    return primoList


verifyPrimoInList([1,2,3,4,5,6,7,8,9,10,11])

# 3) Crear una función que reciba una lista de numeros
#    Devolver el que más se repite
#    Cuántas veces lo hace. 
#    Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:
from collections import Counter

def numRepeated(lis):
    listOfTuples = []

    for number in lis:
        freq = Counter(lis).get(number)
        if(not(number, freq) in listOfTuples):
            newTuple = (number, freq)
            listOfTuples.append(newTuple)
    print(listOfTuples)
    return "El más repetido es el numero " + str(listOfTuples[0][0]) + ". Y se repite " + str(listOfTuples[0][1]) + " veces"
    

numRepeated([1,3,2,3,5,6,1,2,3,1,1,1,3,3])

# 4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.

# In[45]:

def numRepeated(lis, order):
    listOfTuples = []

    if(len(lis)> 0):
        for number in lis:
            freq = Counter(lis).get(number)
            if(not(number, freq) in listOfTuples):
                newTuple = (number, freq)
                listOfTuples.append(newTuple)

    if order == "minor":
        ordenados = sorted(listOfTuples, reverse=True)
        return "El menos repetido es " + str(ordenados[0][0]) + ". Y se repite " + str(ordenados[0][1]) + " vez o veces"
    return "El más repetido es el numero " + str(listOfTuples[0][0]) + ". Y se repite " + str(listOfTuples[0][1]) + " veces"
    

numRepeated([1,3,2,3,5,6,1,2,3,1,1,1,3,3], "mayor")

# 5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
#    Fórmula 1	: (°C × 9/5) + 32 = °F<br>
#    Fórmula 2	: °C + 273.15 = °K<br>
#    Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:
def convertTemperatures(value, originTemp, convertTemp):
    if(originTemp == "C" and convertTemp == "F"):
        return (value * 9) / 5 + 32
    elif(originTemp == "C" and convertTemp == "K"):
        return value + 273.15
    elif(originTemp == "F" and convertTemp == "C"):
        return (value - 32) * 5 / 9
    elif(originTemp == "F" and convertTemp == "K"):
        return (value - 32) * 5 / 9 + 273.15
    elif(originTemp == "K" and convertTemp == "C"):
        return value - 273.15
    else:
        return (value * 9) / 5 - 459.67

convertTemperatures(373, "K", "F")

# 6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:

print("De Celsius a Kelvin: ", convertTemperatures(1, "C", "K"))
print("De Celsius a Farenheit: ", convertTemperatures(1, "C", "F"))
print("De Farenheit a Kelvin: ", convertTemperatures(1, "F", "C"))
print("De Farenheit a Celsius: ", convertTemperatures(1, "F", "K"))
print("De Kelvin a Celsius: ", convertTemperatures(1, "K", "C"))
print("De Kelvin a Farenheit: ", convertTemperatures(1, "K", "F"))

# 7) Armar una función que devuelva el factorial de un número. 
#    Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o
#    negativo

# In[65]:

# 4 * 3 * 2 * 1
def factorial(num):
    if(num > 0 and type(num) == int):
        if(num > 1):
            num = num * factorial(num-1)
    else:
        return "El numero debe ser positivo y entero"
    return num

factorial(4)

# %%
