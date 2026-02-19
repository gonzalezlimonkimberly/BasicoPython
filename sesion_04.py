print("=== Calculadora ===")

num_1 = float(input("Primer numero: "))
num_2 = float(input("Segundo numero: "))
operacion = input("Operacion (+, -, *, /): ")

def calculadora(num_1, num_2, operacion):
    if operacion == "+":
        return num_1 + num_2
    if operacion == "-":
        return num_1 - num_2
    if operacion == "*":
        return num_1 * num_2
    if operacion == "/":
        if num_2 == 0:
            return "No se puede dividir entre 0"
        return num_1 / num_2
    return "Operacion no valida"

print("Resultado:", calculadora(num_1, num_2, operacion))