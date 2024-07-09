###############################################
#
#              PROGRAMA 10
#            TÍTULO:BUCLES LOOPS CICLOS
#
##############################################

"""
NOTA: Bucle/ciclo/loop son términos equivalentes 
Se utiliza para pasar por un mismo código x veces (como ya sabemos)
"""

#EMpezamos a ver las diferentes formas de realizar ciclos.

#####################################################
#                       WHILE
#####################################################

"""
El while siempre va a tener una condición asociada
"""
mi_condicion=0
while(mi_condicion<10):
    print(f"El valor de mi condición es: {mi_condicion}")  #Si la condición nunca cambia esto es un bucle infinito de manual
    mi_condicion += 1
else:
    print("Mi condición es mayor o igual que 10")         #Esto está genial ya que  en la condición saliente pasa por el else


"""
Otra estructura particular del while
"""
mi_condicion=0
while(mi_condicion<10):
    print(f"El valor de mi condición es: {mi_condicion}")  #Si la condición nunca cambia esto es un bucle infinito de manual
    mi_condicion += 1
if (mi_condicion == 10):        #Este if no pertenece al while como el else del caso anterior
    print("Mi condición es igual 10")
else:
    print("Mi condición es mayor o igual que 10")         #Esto está genial ya que  en la condición saliente pasa por el else

#Nos acepta el else pero no el elif. 



print("La ejecución continúa")
