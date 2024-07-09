###############################################
#
#              PROGRAMA 4
#            TÍTULO:STRINGS
#
##############################################

mi_string="Es mi string"
mi_otro_string="Este es mi otro string"

print(len(mi_string))
print(len(mi_otro_string))

print(mi_string + " " + mi_otro_string)

mi_string_con_salto="Este es un string\ncon salto de línea"
print(mi_string_con_salto)

mi_string_con_tabulacion="Este es un string\tcon tabulación"
print(mi_string_con_tabulacion)

mi_string_escapado="\\t Este es un string \\n escapado"
print(mi_string_escapado)


######################################
#       Formateo de Strings
#####################################
name, surname, edad = "Miguel", "Méndez", 30

print("Mi nombre es {} {} y mi edad es {}".format(name,surname,edad)) #Esto es muy usual para configurar distinitos idiomas #Para trabajar con el objeto
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,edad))      #Para trabajar con el número formateado (Tiene que estar con el tipo especificado)

#La forma más a lo burro va a seguir siendo esta, pero cuesta más ejecutarlo (forma menos sutil):
print("Mi nombre es " + name + " " + surname +" y mi edad es "+ str(edad))


#Por inferencia de datos:
print(f"Mi nombre es {name} {surname} y mi edad es {edad}") #Esta dicen en el curso que es la forma mejor (más rápida)
                                                            #La f sirve para formatear y que vaya infiriendo el valor de las variables

######################################
#       Desempaquetado de caracteres
#####################################

#Se van repartiendo los caracteres del string por las variables
lenguaje = "Python"
a, b, c, d, e, f =lenguaje
print(a)
print(e)


#################################
#       Division de cadenas
#################################
lenguaje_slice = lenguaje[1:3]  #En este caso pilla las letras 1 y2
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:]  #En este caso pilla las letras 1 al final
print(lenguaje_slice)

lenguaje_slice = lenguaje[:4]  #En este caso pilla las 4 primerasletras 
print(lenguaje_slice)

lenguaje_slice = lenguaje[-2]  #En este caso pilla la penultima letra
print(lenguaje_slice)

lenguaje_slice = lenguaje[0:6:2]  #En este caso pilla el caracter 0 el 2 y el 4
print(lenguaje_slice)

#################################
#      Reverse de cadenas
#################################

lenguaje_reverse = lenguaje[::-1]  #En este caso pilla lel reverso
print(lenguaje_reverse)


#################################
#      Funciones de cadenas
#################################
print(lenguaje.capitalize())        #Se pone la primera letra en mayúscula
print(lenguaje.upper())             #Se pone todo en mayúscula
print(lenguaje.count("t"))          #Cuentan cuantas t hay en la cadena
print(lenguaje.isnumeric())         #Evalúa si es numérico (si fuese "3" sería TRUE)
print(lenguaje.lower())             #Se pone todo en minúscula
print(lenguaje.upper().isupper())   #Pone en mayúscula y mira si está en mayúsculas
print(lenguaje.lower().isupper())   #Pone en minúscula y mira si está en mayúsculas
print(lenguaje.startswith("Py"))    #Empieza por..
print("Py" == "Py")                 #Evalúa si son iguales

