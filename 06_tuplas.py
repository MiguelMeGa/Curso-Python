###############################################
#
#              PROGRAMA 6
#            TÍTULO:TUPLAS
#
##############################################

#Una tupla es un conjunto de valores invariables

mi_tupla = tuple()  #Esto es una tupla y el constructor se parece a una lista
mi_otra_tupla=()

mi_tupla = (30, 1.68, "Miguel", "Méndez") #Fiajmos valores en la tupla
mi_otra_tupla = (50, 60, 70)              #Fijamos valores en la otra tupla

print(f"Esta es mi turpla: {mi_tupla}")  #Este es ele listado de valores de la tupla 
print(type(mi_tupla))                    #Me dé un tipo tupla

#Se puede acceder a elementos  igualmente que en una lista
print(mi_tupla[0])      #Accedemos al primer elemento de la tupla
print(mi_tupla[-1])     #Accedemos al último elemento de la tupla
#print(mi_tupla[4])      #error
#print(mi_tupla[-6])     #error

#En este caso no hay operaciones de inserción ya que como hemos dicho son invariables
print(mi_tupla.count("Miguel"))   #El count funciona igual
print(mi_tupla.index("Méndez"))   #Nos indica el primer índice que encuentra con la palabrqa en cuestión

#mi_tupla[1]=1.68 #Error las tuplas son inmutables
#mi_tupla[5]=1.8 #Error las tuplas son inmutables no se pueden modificar


#################################################
#           Concatenación de tuplas
#################################################
mi_tupla_concatenada = mi_tupla + mi_otra_tupla
print(f"Mi tupla concatenada es: {mi_tupla_concatenada}")

print(f"Mi parte de la tupla es: {mi_tupla_concatenada[3 : 6]}")    #Para imprimir un rango lo hacemos con : 

#####################################################
#           NOTA: UNA LISTA MUTABLE ES UNA TUPLA
######################################################

#Se puede pasar una tupla a una lista, sin problema ninguno
mi_tupla_trans= list(mi_tupla)
print(f"Esta es mi nueva lista: {mi_tupla_trans} cuya clase es:{type(mi_tupla_trans)}")

mi_tupla_trans[2]="Mouredev"
mi_tupla_trans.insert(1, "Azul")
print(f"Mi lista es:{mi_tupla_trans}")

#Ahora podemos volver transformar la lista en tupla sin problema
mi_tupla_trans=tuple(mi_tupla_trans)
print(f"Esta es mi nueva tupla: {mi_tupla_trans} cuya clase es:{type(mi_tupla_trans)}")

###################################################################
#Borrar una tupla la idea es que si no la  podemos modificar no se puede borrar
####################################################################

del mi_tupla #Se borra toda la tupla la variable (Entera)
#print (mi_tupla)  #Esto va a dar un error!!!
#En la lista se usa el cleafr para limpiar todos los valores