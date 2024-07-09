###############################################
#
#              PROGRAMA 7
#            TÍTULO:SETS
#
##############################################

"""
    Un set es una estructura de datos:
    1 No ordenada.
    2 No admite repetidos.
    3 No se puede acceder por posición.
    4 guarda los elementos de forma única.
    5 Un HAsh interno guarda los elementos.

    ¿Ventajas?
    No trabaja con datos repetidos y 
    trabaja bien con estructuras de datos
    que no queremos que estén ordenados
"""

mi_set = set()           #Creamos el tipo de dato set
mi_otro_set = {}         #Los diccionarios y los sets se definen de igual manera (tienen la misma estructura)

print(type(mi_set))          #Se crea el tipo  de dato set
print(type(mi_otro_set))     #Nos dice que inicialmente es un diccionario

#Pero vamos a dar valores a mi_otro_set
mi_otro_set = {"Pepe" , "Paco" , "Luis"}
print(f"Especificación de mi set: {mi_otro_set}") 
print(type(mi_otro_set))#Comprobamos que ahora el tipo es set


#Operaciones con set
print(len(mi_otro_set))



# Acceder a un elemento del set
#print(mi_otro_set[1])#Nos da error -> No podemos 

mi_otro_set.add("Jacobo")  #Añade JAcobo al  set
print(mi_otro_set)         #Vemos que un set no es una estructura ordenada, Utiliza un HASH para meter los elementos
                            #Mete elementos de forma desordenada

mi_otro_set.add("Jacobo")   #Solamente se incluye un JAcobo luego un set no admite  repetidos 
print(mi_otro_set)              


##################################
#       Busquedas en los set
##################################

print("Pepe" in mi_otro_set)     #Comprobación de si Pepe existe en la lista
print("Jose" in mi_otro_set)     #Comprobación de si Jose existe en la lista que en este caso no está

##################################
#     Borrar elementos en los set
##################################
mi_otro_set.remove("Jacobo")        #Se borran elementos en los set
print(mi_otro_set)                  #Se comprueba que se ha borrado el elemento 

mi_otro_set.clear()                #Se borran todos los elementos del set
print(len(mi_otro_set))


"""
del mi_otro_set #Se borra la variable el objeto
print(mi_otro_set)  #Luego esto dará error
"""

#################################
#   CAMBIOS DE SET A LISTA
#################################

mi_set = {"Pepe" , "Paco" , "Luis"}
mi_lista = list(mi_set)
print(f"Esta es mi nueva lista {mi_lista} con el tipo {type(mi_lista)}")

print(mi_lista[0])      #En una lista podemos acceder ya amun determinado elemento
#Esto es muy arriesgado ya que como vimos la primera vez el set se creó con un orden y la segunda con otro


###############################
# VAMOS A UNIR LOS SETS
##############################

mis_lenguajes = {"Kotlin","Swift", "Python"}
mi_nuevo_set = mi_set.union(mis_lenguajes)
print(f"ESte es mi nuevo set:{mi_nuevo_set}")
#Si repetimos nuevamente el proceso de unión -> No pasaría nada ya que replicaríamos elementos y no se duplican
mi_nuevo_set_2 = mi_nuevo_set.union(mis_lenguajes).union({"C", "C#", "Java"})
print(f"Este es mi nuevo set:{mi_nuevo_set_2}")   #como vemos solamente se introducen los nuevos elementos

#################################
#   OPERACIÓN DIFERENCIA
##################################

mi_set_diferencia = mi_nuevo_set_2.difference(mi_nuevo_set)
print(f"Mi set diferencia: {mi_set_diferencia}")  #como vemos la diferecia es el  set introducido 