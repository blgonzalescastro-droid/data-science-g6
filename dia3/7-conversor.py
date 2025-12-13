import os
import math
# CALCULADORA CONVERSOR DE DIVISAS
salir = "no"
while(salir == "no"):
    os.system("clear")
    # ENTRADA
    print("================ CONVERSOR DE DIVISAS ===============")
    
    print("             Tipo de cambio del mercado")
    print("                  $1 USD = 3.0 PEN ")
    
    print("========= OPCIONES ========")
    print("1. Deseo cambiar USD a PEN")
    print("2. Deseo cambiar PEN a USD")
    opcion = int(input("Ingrese la opcion que desea: "))
    if opcion == 1:

        cantidad = int(input("Cantidad USD: "))
        tipo_de_cambio = int(3)
        # PROCESO
        opcion == 1
        operacion = "usdtopen"
        resultado = cantidad * tipo_de_cambio
    elif opcion == 2:
        cantidad = int(input("Cantidad PEN: "))
        tipo_de_cambio = int(3)
        opcion == 2
        operacion = "pentousd"
        resultado = cantidad / tipo_de_cambio
    else:
            print("Operación no válida")
            exit()

    # SALIDA
    if opcion == 1:
        print(f"{cantidad} USD = {resultado} PEN")
    elif opcion == 2:
        print(f"{cantidad} PEN = {resultado} USD")
    salir = input("Desea salir? (si/no): ")
    if salir == "si":
        break