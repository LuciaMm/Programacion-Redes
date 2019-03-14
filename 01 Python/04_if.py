#Crear un script en el que guardéis en una variable un número
x = int(input("Introduzca un número: "))
#Controlar el tamaño del número en 4 rangos (menor de 20, entre 20 y 39, entre 40 y 59, mayor de 60)
if x < 20:
  print(str(x) + " es menor que 20.")
elif x >= 20 and x <= 39:
  print(str(x) + " está entre 20 y 39.")
elif x >= 40 and x <= 59:
  print(str(x) + " está entre 40 y 59.")
else:
  print(str(x) + " es mayor que 60.")
#En cada uno de los casos imprimir por pantalla el número que se haya introducido.