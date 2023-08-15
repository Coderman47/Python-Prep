#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:
new_list = []
i = -15
while(i < 0):
    new_list.append(i)
    i+=1

print(new_list)



# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:
length = len(new_list)
i = 0
while i < length:
    if(new_list[i] % 2 == 0):
        print(new_list[i])
    i+=1




# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:

for num in new_list:
    if(num % 2 == 0):
        print(num)



# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:
vueltas = 1
for num in new_list:
        print(num)
        if(vueltas == 3):
            break
        vueltas += 1


# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:
i = 0
new_list.sort(reverse=True)
for num in enumerate(new_list):
     print(num)



# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:

number_list = [1,2,5,7,8,10,13,14,15,17,20]

# In[11]:


n = 1
while(n<=20):
    if(not(n in number_list)):
            number_list.insert((n-1),n)
    n += 1

print(number_list)



# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:
fibo=[0,1]
n=2
while(n<30):
    fibo.append(fibo[n-1]+fibo[n-2])
    n+=1

print(len(fibo))



# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:

sum(fibo)


# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:

primeros= 13
n = primeros - 5
while(n<13):
    print(fibo[n]/fibo[n-1])
    n+=1


# 10) A partir de la variable cadena ya dada, 
# Mostrar en qué posiciones aparece la letra "n"<br>

# In[39]:

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
for letter in enumerate(cadena):
    if(letter[1]=="n"):
        print("Aparece en el index: ",letter[0])


# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:
diccionario = {"nombre":["luciano", "fernando", "julian", "julio"], "apellido": "Navarro", "pais":["Argentina", "Italia", "Estados Unidos"]}

for clave in diccionario.keys():
     print(clave)

# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[45]:
lista = list(cadena)

print(lista)
n=0
while(n<len(lista)):
    print(cadena[n])
    n+=1

# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:
lista1 = [2,3,4,5,0]
lista2 = [1,2,3,4,0]

combinacion=zip(lista1,lista2)

print(type(combinacion))
for elemento in combinacion:
     print(elemento)



# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>

# In[49]:
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
newList = []

for number in lis:
    if(number % 7 == 0):
        newList.append(number)

print(newList)

# 15) A partir de la lista de a continuación 
#     Contar la cantidad total de elementos que contiene, teniendo en cuenta
#     que un elemento de la lista podría ser otra lista:<br>

# In[56]:
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres'], "triste"]
countElements = 0

for element in lis:
    if(type(element) == list):
        countElements = countElements + 1 + len(element)
    else:
        countElements +=1

print("Cantidad total:",countElements)

# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:
for indice ,element in enumerate(lis):
    if(type(element) != list):
        lis[indice] = [element]

print(lis)



# %%

lis = "que onda con el queso que parece que quiere irse"
qus = [letter for letter in lis if letter == "q"]
print("Cantidad de Q:",len(qus))
# %%
