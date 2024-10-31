#luis jose diaz urieles
#31/10/2024
#grupo 2 semestre 5

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

# Uso de la calculadora
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")

if operacion == '+':
    print(f"Resultado: {suma(a, b)}")
elif operacion == '-':
    print(f"Resultado: {resta(a, b)}")
elif operacion == '*':
    print(f"Resultado: {multiplicacion(a, b)}")
elif operacion == '/':
    print(f"Resultado: {division(a, b)}")
else:
    print("Operación no válida.")
