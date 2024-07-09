###############################################
#
#              PROGRAMA 8
#            TÍTULO:DICCIONARIOS
#
##############################################
"""
    Un diccionario utiliza un hashback por dentro:
    Pero hay lenguajes de programación que lo llamas mpas, otros hashmaps...

    Aquí vamos a hablar de pares clave-valor:
    En algunos casos la clave será un String y en otras un valor numérico

"""


mi_diccionario = dict()   #Se crean de igual manera
mi_otro_diccionario = {}   #Se crean de la misma forma
print("Tipo de diccionario:", type(mi_diccionario))
print("La otra forma de definir un diccionario:", type(mi_otro_diccionario))

################################################
#           DEFINICIÓN DE DICCIONARIOS
################################################
mi_otro_diccionario = {"Nombre":"Miguel" , "Apellido":"Méndez" , "edad":30 ,1:"Python"}   #Como vemos esto se está agupando por pares de valores
                     #Esto sería un objeto similar a un objeto como un JSON

mi_diccionario = {
                  "Nombre":"Miguel" , 
                  "Apellido":"Méndez" , 
                  "edad":30, 
                  "Lenguajes": {"Python", "C", "Kotlin"}, #Como clave tiene el Sting y como valor un set
                  1:1.68
                  }  

print(mi_diccionario)
print(mi_otro_diccionario)

######################################
#   Miramos la longitud del diccionario 
#######################################

print(f"La longitud del diccionario es: {len(mi_diccionario)}")  #La longitud se corresponde con el número de claves de este 
print(mi_diccionario["Nombre"])  #Se imprime el valor asociado a la clave


######################################
#   Actualizar un diccionario
######################################
mi_diccionario["Nombre"] = "Pepe"       #Solamente accederemos a la clave y modificaremos el valor esta es la forma de modificarlo
print(mi_diccionario)                   #Me devuelve el diccionario completo

print(mi_diccionario[1])                #Vamos a acceder a una clave numérica

######################################
# Añadir un campo al diccionario 
######################################
mi_diccionario["Pueblo"] = "Piñeira" #Vamos en este punto añadir un campo nuevo al diccionario en cuestión 
print(mi_diccionario)            #Como vemos se añade una nueva estructura del tipo clave-valor que es pueblo.

#####################################
#   Borrar cosas de un diccionario
#####################################
del(mi_diccionario["Pueblo"])   #Como vemos así eliminamos un solo elemento en nuestro diccionaroio
print(mi_diccionario)           #Al imprimir esto nos queda sin el elemento diccionario


################################################
#   Comprobaciones de si está en el diccionario
################################################

print("Méndez" in mi_diccionario["Apellido"])  #Esta estructura tiene que evaluarse considerando la clave
print("Apellido" in mi_diccionario)            #Considera que apellido si es uno de los campos tiene presencia dentro del diccionario


###############################################
#   OPERACIONES SOBRE EL DICCIONARIO
###############################################

print(mi_diccionario.items())               #Toma una lista de las parejas de clave valor para todos los elementos del diccionario
print(mi_diccionario.keys())                #Toma una lista de las claves de los elementos del diccionario
print(mi_diccionario.values())              #Se toman los valores propios del diccionario

############################################
# Creación de un diccionario vacío
############################################

mi_nuevo_diccionario=dict.fromkeys(("Nombre", 1, "Piso"))  #Crea un nuevo diccionario vacío poniendole las claves que le marcamos ahí
print(mi_nuevo_diccionario)                                #Esta es una forma de crear un diccionario

mi_nuevo_diccionario_2=dict.fromkeys(mi_diccionario)       #En este caso crea el diccionario con las claves de mi diccionario
print(mi_nuevo_diccionario_2)                              #Se realiza en efecto una copia de este diccionario

mi_nuevo_diccionario_2=dict.fromkeys(mi_diccionario, ("Brais", "Moure"))        #Ahora vamos a meterle valores
print(mi_nuevo_diccionario_2)                                                   #Se mete a todos los valores del diccionario: Brais y Moure

mi_nuevo_diccionario_2=dict.fromkeys(mi_diccionario,  "Moure")                  #Ahora vamos a mete el valor moure a todos los elementos de la lista
print(mi_nuevo_diccionario_2)                                                   #Se mete a todos los valores del diccionario:  Moure

############################################
# Pasar a lista, tuplas y sets el diccionario
############################################


print(mi_nuevo_diccionario_2.values())                      #Toma los valores del nuevo diccionario 2
print(list(mi_nuevo_diccionario_2))                         #Transforma en lista las claves del diccionario especificado
print(tuple(mi_nuevo_diccionario_2))                        #Idem com tuplas
print(set(mi_nuevo_diccionario_2))                          #Idem respecto a sets