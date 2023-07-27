# Crear un set 

my_set = {1, 2, 3, 4, 5}

# Agregar elementos al set

my_set.add(6)
print(type(my_set))
print(my_set) # {1, 2, 3, 4, 5, 6}

# Eliminar elementos del set
my_set.remove(2)
print(my_set) # {1, 3, 4, 5, 6}

# Realizar operaciones de conjuntos

set1= {1, 2, 3}
set2= {3, 4, 5}

union = set1 | set2
print(union) # {1, 2, 3, 4, 5}

interseccion = set1 & set2
print(interseccion) # {3}

diferencia = set1 - set2
print(diferencia) # {1, 2}

diferencia_simetrica = set1 ^ set2
print(diferencia_simetrica) # {1, 2, 4, 5}
