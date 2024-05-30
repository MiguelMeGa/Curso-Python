###############################################
#
#              PROGRAMA 3
#            TÍTULO:OPERADORES
#
##############################################

######################################
#       Operadores aritméticos
#####################################

print(3 + 4)  #Operador suma
print(3 - 4)  #Operador resta
print(3 * 4)  #Operador multiplicación
print(3 / 4)  #Operador división
print(3 % 4)  #Operador módulo (me queda el resto)
print(10 % 3)

#Python ganó adeptos por su capacidad de cálculo

print(10 // 3) #División entera (aproximada)
print(2 ** 3)  #Exponente 2^3

#Cadenas con operadores
print("Hola"+"Pepe"+"!!") #Quedará HolaPepe (Concatenar)
print("Hola"+str(5))
print("Hola " * 5)         #Imprime la palabra Hola 5 veces (solamente funciona con enteros)
print("hola " * int(3.0))

######################################
#       Operadores comparativos
#####################################

# Con números:
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(3 > 4 >2)

#Con cadenas:
#Evalúa en una ordenación alfabética cual es el mayor (Imagino que sea con la suma de códigos Ascci)

print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")


######################################
#       Operadores lógicos
#####################################
"""
    Hay tres operadores lógicos:
    and
    or
    not
"""

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 > 4 or "Hola" < "Python")
print(not("Hola" > "Python"))
print (3 < 4 or ("Hola" > "Python" and 4==4)) #Establecer órdenes de prioridad
print(not(False))