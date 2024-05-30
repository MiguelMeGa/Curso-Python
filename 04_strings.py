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

#Se bvan repartiendo los caracteres del string por las variables