###############################################
#
#              PROGRAMA 5
#            TÍTULO:LISTAS
#
##############################################

#Nota: una lista es algo más complejo que un array y se puede ordenar, insertar, recolocar, hacer operaciones complejas sobre él...
#Python es un lenguje orientado a objetos, luego puede extender sus objetos de algo básico que puede ser un objeto

mi_lista = list()   #Esto es una lista. Entendemos lista como un conjunto de datos
mi_otra_lista = []  #Esto es otra lista La definición es igual

print(len(mi_lista)) #Actualmente la longitud de la lista va a ser 0 pero está preparada para añadir datos (objetos)

mi_lista = [35, 24, 62, 52, 30, 30, 17 ]  #Esto es una lista: una forma de agrupar datos
print(mi_lista)

mi_otra_lista = [30, 1.68, "Miguel","Méndez"]   #Se tiene igualmente una lista pero con otro tipos
print(type(mi_otra_lista))                    #Me dice que es una lista. aquí no existe el array como tal
print(mi_otra_lista)

print(mi_lista[0])   #Se accede al primer elemento de la lista
print(mi_lista[1])   #Se accede als elemento 1 de la lista
print(mi_lista[-1])  #Se accede al ultimo elemnto de la lista
print(mi_lista[-3])  #Se accede al antepenultimo elemnto de la lista
#print(mi_lista[-8]) Error! Esto petaría el sistema
#print(mi_lista[8]) Error! Esto petaría el sistema

print(len(mi_lista))            #Esto evalúa la longitud de mi lista 
print(mi_lista.count(30))       #Esto cuenta el número de elementos de la lista que tienen ese valor pasado como parámetro

#######################################
#   Desempaquetado de listas
######################################

edad, altura, nombre, apellido = mi_otra_lista  #Descomposición de elementos de una lista 
print(f"Esta es mi edad {edad}")

edad, altura, nombre, apellido = mi_otra_lista[0], mi_otra_lista[1], mi_otra_lista[2], mi_otra_lista[3]
print(f"Este es mi apellido {apellido}")

#######################################
#   COncatenación de listas
######################################
mi_lista_concatenada = mi_lista + mi_otra_lista                 #Se concatena en el orden especificado
print(f"Esta es una lista concatenada: {mi_lista_concatenada}")

#Ejemplificación de los lenguajes de tipo dinámico
mi_lista = "Hola Python"
print(mi_lista)             #Como vemos pisa el contenido previo de mi lista y esto es peligroso ya que pasaría a ser un stringjj

mi_lista = [35, 24, 62, 52, 30, 30, 17 ]  #Esto es una lista: una forma de agrupar datos


######################################
#   OPERACIONES SOBRE LISTAS
######################################

mi_nueva_lista = [30, 1.68, "Miguel","Méndez"]      #Esta es una copia de la lista que tenía anteriormente
mi_nueva_lista.append("Gayol")                      #Para añadir nuevos elementos al final de la lista vamos a append
print(f"Mi lista quedará así: {mi_nueva_lista}")    #La forma en la que quedará la lista con el ultimo elemento al final

mi_nueva_lista.insert(1,"verde")                    #Inserción de un elemento en la posición especificada de mi color favorito
print(f"Mi lista quedará así: {mi_nueva_lista}") 

mi_nueva_lista.remove ("verde")                     #Eliminación de un elemento de la lista
print(f"Mi lista quedará así: {mi_nueva_lista}") 

valor_quitado = mi_lista.pop()                      #Desapila el ultimo valor de la lista
print(f"El valor quitado de la lista es: {valor_quitado}") 
print(f"La lista quedaría: {mi_lista}")

valor_quitado = mi_lista.pop(2)                     #quita un elemento en la posición indicada de la lista
print(f"El valor quitado en el indice 2 de la lista es: {valor_quitado}") 
print(f"La lista quedaría: {mi_lista}")

print(f"La lista antes de eliminar el elemento 2 sería: {mi_lista}")
del mi_lista[2]                                 #Si simplemente me quiero cargar un elemento de la lista hacemos un del no hace falta hacer un pop
print(f"La lista eliminando el elemento 2 quedaría: {mi_lista}")

mi_lista.clear()                                #Hacemos clear sobre la lista
print(f"Mi lista quedaría vacía: {mi_lista}")


#################################
#
#       IMPORTANTE:
#
# El remove se hace para un valor que sabemos que está dentro ejemplo: mi_lista.remove(30) -> Elimina el primer 30 que encuentra
# EL del se hace con una posición  concreta que queremos eliminar del mi_lista[2]
#
##################################################################################

mi_nueva_lista[1]=1.85
print(f"Cambio el valor de la altura en mi lista: {mi_nueva_lista}")

mi_lista_copia = mi_nueva_lista.copy()                  #Esta es la copia de mi lista
print(f"La copia de mi lista es: {mi_lista_copia} ")

#Finalmente le hacemos un reverse a la lista copiada
mi_lista_copia.reverse()
print(mi_lista_copia)


#Definimos nuevamente los valores de mi_lista
mi_lista = [35, 24, 62, 52, 30, 30, 17 ]  #Esto es una lista: una forma de agrupar datos
mi_lista.sort()                           #Ahora ordenamos los eleemntos de la lista por defecto los hace de menor a mayor
print(f"Vamos a ordenar los elementos de la lista: {mi_lista}")

#######################################
#
#       Como hacer sublistas
#
######################################

mi_sublista=mi_lista[2:4]
print(f"Esta es mi sublista: {mi_sublista}")