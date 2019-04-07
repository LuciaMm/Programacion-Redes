def calculadora():
  #Crear las sentencias necesarias para recoger dos números a través del terminal
  try:
    a = int(input("Número A: "))
    b = int(input("Número B: "))
    #break
  

    #Integrar funcionalidades de suma, resta, multiplicación, división, y exponencial
    #Implementar funciones, diccionarios, y excepciones
    def suma():
      return a+b

    def resta():
      return a-b

    def multiplicacion():
      return a*b

    def division():
      return a/b

    def exponencial():
      return a**b

    #Permitir escoger el modo de operación de forma manual (el usuario ha de introducir un número para que sepa qué operación realizar)
    op = int(input("Escoja operación:\n 1.- Suma\n 2.- Resta\n 3.- Multiplicación\n 4.- División\n 5.- Exponencial\n"))

    operaciones = {1: suma(), 2: resta(), 3: multiplicacion(), 4: division(), 5: exponencial()}
    simbolo = {1: ' + ', 2: ' - ', 3: ' * ', 4: ' / ', 5: " ^ "}

    if operaciones[op] == 5 or b == 2:
      print(str(a) + " al cuadrado = " + str(operaciones[op]))
    elif (b == 3):
      print(str(a) + " al cubo = " + str(operaciones[op]))
    else:
      print(str(a) + simbolo[op] + str(b) + " = " + str(operaciones[op]))
  except ValueError:
    print("Por favor, inserte un número")
    calculadora()