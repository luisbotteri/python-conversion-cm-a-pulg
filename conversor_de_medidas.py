print("""¡Hola! Beinvenido/a al conversor de medidas.
      Este programa te ayudará a transformar medidas de muebles de cm a pulg.""")

while True:
    print("Elija una de las siguientes opciones\n"
              "1. De pulg a cm.\n"
              "2. De cm a pulg.\n" \
              "3. Salir.")
    opcion = input("Opción: ").strip()
    if not opcion:
        print("No ingresaste ninguna opción. Por favor, intentá de nuevo.")
        continue

    if opcion == "1":
        try:
            print("Has seleccionado la opción 1.")
            valores_pulg = list(map(float, input("Por favor, ingresa los valores que deseas convertir (pulg) separados por espacio.\n"
             "Ejemplo: 1 2 3: ").split()))
            print("Los valores ingresados son: ", valores_pulg)
            conversion = [round(pulg * 2.54, 2) for pulg in valores_pulg]
            print("Las medidas en centímetros son: ", conversion)
        except ValueError:
            print("Valores no válidos. Ingrese nuevamente los datos.")
    
    elif opcion == "2":
        try:
            print("Has seleccionado la opción 2.")
            valores_cm = list(map(float, input("Por favor, ingresa los valores que deseas convertir (cm) separados por espacio.\n"
             "Ejemplo: 1 2 3: ").split()))
            print("Los valores ingresados son: ", valores_cm)
            conversion = [round(cm / 2.54, 2) for cm in valores_cm]
            print("Las medidas en pulgadas son: ", conversion)
        except ValueError:
            print("Valores no válidos. Ingrese nuevamente los datos.")
    
    elif opcion == "3":
        print("¡Gracias por utilizar nuestra herramienta de conversión!")
        break
   
    else:
        print("Opción no válida. Ingrese 1, 2 o 3.")

    