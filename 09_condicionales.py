###############################################
#
#              PROGRAMA 9
#            TÍTULO:CONDICIONALES
#
##############################################
"""
    Los condicionales permiten establecer 
    flujos de ejecución en el código
"""
mi_condicion = True

if(mi_condicion == True):        #Se establece la primera condición 
    print("Soy true")
else:
    print("Soy false")

print("Le ejecución condicional ha terminado")


"""
    Condicionales con valores enteros
"""

mi_condicion=2*5

if(mi_condicion>10):
    print("EL valor es mayor que 10")
else:
    print("EL valor es menor igual que 10")




"""
    Más de una condición en el condicional
"""
if(mi_condicion>10 and mi_condicion<20):
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor que 10 o mayor que 20")


"""
    Estructura con el elif
"""
mi_condicion=25

if(mi_condicion>10 and mi_condicion<20):
    print("Es mayor que 10 y menor que 20")
elif(mi_condicion > 20):
    print("Es mayor que 20")
else:
    print("Es menor que 10")

print("La ejecución continúa")

"""
    Estructura con el elif compuesta
"""
mi_condicion=25

if(mi_condicion>10 and mi_condicion<20):
    print("Es mayor que 10 y menor que 20")
elif(mi_condicion > 20):
    print("Es mayor que 20")
elif(mi_condicion > 22):
    print("Es mayor que 22")
else:
    print("Es menor que 10")


"""
    Estructura con el elif compuesta
"""
mi_condicion=25

if(mi_condicion>10 and mi_condicion<20):
    print("Es mayor que 10 y menor que 20")
elif(mi_condicion == 25):
    print("Es igual a 25")
else:
    print("Es menor que 10")


"""
    Comparación  de cadenas vacías
"""
mi_cadena=""

if mi_cadena == "":
    print("La cadena está vacía")
else:
    print("La cadena no está vacía")


"""
    Casos particulares
"""
mi_cadena = "Mi cadena de texto"

if mi_cadena == "Mi cadena de textooooo":
    print("Estas cadenas de texto coinciden")   #En este caso no coinciden


"""
    Comprobación de que mi cadena de texto está vacía
"""
mi_cadena=""
if(not mi_cadena):
    print("Mi cadena de texto es vacía")


print("La ejecución continúa")