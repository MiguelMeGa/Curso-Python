###############################################
#
#              PROGRAMA 2
#            TÍTULO:VARIABLES
#
##############################################

"""
    Nota: por convenio en python vamos a escribir las variables como snake case:
    En lugar de : micasa
    será -> mi_casa
"""

#Definición de una variable de tipo str

my_string_variable="Hola chato"
print(my_string_variable)

#Definición de una variable de tipo int

my_int_variable=5
print(my_int_variable)

#Vamos a hacer un print con multiples elementos

print(my_string_variable,my_int_variable) #con la , mete varios datos en una cadena

#Veamos qué pasa si pasamos una variable int a string

my_int_str_variable=str(my_int_variable) 
print(my_int_str_variable)               #Imprime un 5 pero del tipo cadena
print(type(my_int_str_variable))

#Print es una función como tal y en realidad no tiene un tipo de dato como tal

#Veamos la función del sistema len()  que nos devuelve
print("Devolvemos la longirud de la cadena",len(my_string_variable))

#Declaración de variables en una sola línea ¡Cuidado con abusar de esto!
name, surname, alias, edad= "Miguel","Méndez","Migue",30
print("Me llamo:",name,surname, ". Mi alias es:",alias,"y tengo",edad)


#Veamos como son aquí los input (es raro de usar Solamente se usan para aplicaciones que trabajan desde el terminal)
"""
nombre_principal=input("Dime el nombre:")
edad_principal=input("Dime la edad:")
print("Mi nombre es:",nombre_principal)
print("Mi edad es:",edad_principal)
"""
#Podemos hacerlo de igual manera con las variables name y edad (ya que son variables)
"""
name=input("Dime el nombre:")
edad=input("Dime la edad:")
print("Mi nombre es:",name)
print("Mi edad es:",edad)
"""
#Podemos además darle a una variable el tipo que nos dé la gana
#Python no tiene un tipado fuerte: y esto a veces es peligroso por si se asigna un valor que no es
name = 123
edad="Hola soy edad"
print(name,edad)

#Hay formas de especificar el tipado pero no podemos forzarlo
adress: str = "Mi direccion"  #Le indicamos que es un string
adress = 32                   #Pero aquí lo pasamos a int
print(type(adress))

"""Nota: Especificar el tipo en los input puede rener más sentido que aquí"""