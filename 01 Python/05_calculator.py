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


    #Realizar las operaciones e imprimir el valor por pantalla.
    if op == 1:
      print("Suma: " + str(a) + " + " + str(b) + " = " + str(suma()))
    elif op == 2:
      print("Resta: " + str(a) + " - " + str(b) + " = " + str(resta()))
    elif op == 3:
      print("Multiplicación: " + str(a) + " * " + str(b) + " = " + str(multiplicacion()))
    elif op == 4:
      try:
        print("División: " + str(a) + " / " + str(b) + " = " + str(division()))
      except ZeroDivisionError:
        print("ERROR: No se puede dividir entre cero")
    elif op == 5:
      if b == 2:
        print("Exponencial: " + str(a) + " elevado al cuadrado = " + str(exponencial()))
      elif b == 3:
        print("Exponencial: " + str(a) + " elevado al cubo = " + str(exponencial()))
      else:
        print("Exponencial: " + str(a) + " elevado a " + str(b) + " = " + str(exponencial()))
    else:
      print("Operación no válida. Inténtelo de nuevo")
      calculadora()
  except ValueError:
    print("Por favor, inserte un número")
    calculadora()