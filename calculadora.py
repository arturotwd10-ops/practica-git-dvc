# Modificaciones realizadas en la rama desarrollo
# Proyecto de practica de control de versiones con Git
import math

def calculadora():
    print("=== CALCULADORA CIENTÍFICA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Seno")
    print("8. Coseno")
    print("9. Salir")

    while True:
        opcion = input("\nSelecciona una opción: ")

        if opcion == "9":
            print("¡Hasta luego!")
            break

        if opcion not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("Opción no válida.")
            continue

        try:
            if opcion == "6":
                numero = float(input("Ingresa un número: "))
                if numero < 0:
                    print("No se puede calcular la raíz cuadrada de un número negativo.")
                else:
                    print("Resultado:", math.sqrt(numero))

            elif opcion in ["7", "8"]:
                angulo = float(input("Ingresa el ángulo en grados: "))
                radianes = math.radians(angulo)

                if opcion == "7":
                    print("Resultado:", math.sin(radianes))
                else:
                    print("Resultado:", math.cos(radianes))

            else:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))

                if opcion == "1":
                    print("Resultado:", num1 + num2)
                elif opcion == "2":
                    print("Resultado:", num1 - num2)
                elif opcion == "3":
                    print("Resultado:", num1 * num2)
                elif opcion == "4":
                    if num2 == 0:
                        print("Error: no se puede dividir entre cero.")
                    else:
                        print("Resultado:", num1 / num2)
                elif opcion == "5":
                    print("Resultado:", num1 ** num2)

        except ValueError:
            print("Error: ingresa un número válido.")

if __name__ == "__main__":
    calculadora()
