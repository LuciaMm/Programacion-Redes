#Crear una lista que contenga varios strings.
string_list = ["string1", "string2", "string3", "string4", "string5"]
#Crear una lista que contenga varios integers.
int_list = [1, 2, 3, 4, 5]
#Crear una lista que contenga strings, integers y floats.
mix_list = ["stringA", 6, 1.0, "stringB", 7, 0.75, "stringC", 8, 0.5]
#Crear las sentencias necesarias para imprimir, por pantalla, la información de las listas.
print(string_list)
print(int_list)
print(mix_list)
#Crear 3 sentencias para asignar, en cada una, el último valor de una lista diferente a una variable (es decir, habrá 3 variables, cada una con el último valor de una de las listas).
last_string_list = string_list[-1]
last_int_list = int_list[-1]
last_mix_list = mix_list[-1]
#Crear una sentencia para imprimir, por pantalla, un texto, y concatenar la información de las variables.
print("Last element of string_list: " + last_string_list +
	" // Last element of int_list: " + str(last_int_list) +
	" // Last element of mix_list: " + str(last_mix_list))
#Crear un diccionario de vuestras películas/obras favoritas (clave: autor, valor:película)
movies = {"David Yates": "Harry Potter and the Order of the Phoenix",
"Nick Hurran": "Doctor Who: The Day of the Doctor",
"James Gunn": "Guardians of the Galaxy: Vol. 2",
"Taika Waititi": "Thor: Ragnarok"}
#Crear sentencia para imprimir por pantalla todo el diccionario.
print(movies.items())
#Crear sentencia para imprimir por pantalla sólo las claves del diccionario
print(movies.keys())
#Crear sentencia para imprimir por pantalla sólo los valores del diccionario.
print(movies.values())