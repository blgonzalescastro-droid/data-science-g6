# CALCULADORA

# ENTRADA
numero1 = int (input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operacón a realizar (+,-,*,/) : ")
# PROCESO
if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "x":
    resultado = numero1 * numero2
elif operacion == "/":
    resultado = numero1 / numero2
else:
    print("Operación no válida")
# SALIDA
print(f"{numero1}{operacion}{numero2}= {resultado}")