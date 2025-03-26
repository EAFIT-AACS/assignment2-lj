import random
import time
from pda_tree_builder import PDA, build_tree  # Importamos el PDA con historial

# Función para generar cadenas válidas (S -> aSb | ε)
def generar_cadena_valida(cadenas_generadas):
    opciones = ["ab", "aabb", "aaaabbbb"]
    for opcion in opciones:
        if opcion not in cadenas_generadas:
            cadenas_generadas.add(opcion)
            return opcion
    return ""

# Función para generar cadenas inválidas
def generar_cadena_invalida(cadenas_generadas):
    opciones = ["aabaab", "baaabbaaa", "aaabaabbb"]
    for opcion in opciones:
        if opcion not in cadenas_generadas:
            cadenas_generadas.add(opcion)
            return opcion
    return ""

# Función principal para mostrar las cadenas
def main():
    random.seed(time.time())  # Cambia la semilla en cada ejecución

    cadenas_validas_generadas = set()
    cadenas_invalidas_generadas = set()

    cadenas_validas = [generar_cadena_valida(cadenas_validas_generadas) for _ in range(3)]
    cadenas_invalidas = [generar_cadena_invalida(cadenas_invalidas_generadas) for _ in range(3)]

    pda = PDA()  # Instanciamos el autómata

    # Listas para almacenar los árboles de ejecución
    historias_validas = []
    historias_invalidas = []

    print("Cadenas válidas:")
    for cadena in cadenas_validas:
        aceptada = pda.process_string(cadena)
        resultado = "Aceptada" if aceptada else "Rechazada"
        print(f"Cadena: '{cadena}' -> {resultado}")

        if aceptada:
            historias_validas.append(pda.get_history())

    print("\nCadenas inválidas:")
    for cadena in cadenas_invalidas:
        aceptada = pda.process_string(cadena)
        resultado = "Aceptada" if aceptada else "Rechazada"
        print(f"Cadena: '{cadena}' -> {resultado}")

        if aceptada:  # Aunque no deberían ser aceptadas, guardamos su historia
            historias_invalidas.append(pda.get_history())

    # Imprimir los árboles de derivación
    print("\nÁrboles de derivación para cadenas válidas:")
    for historia in historias_validas:
        build_tree(historia)

    # Mensaje cuando no hay árboles para cadenas inválidas
    print("\nÁrboles de derivación para cadenas inválidas:")
    if historias_invalidas:
        for historia in historias_invalidas:
            build_tree(historia)
    else:
        print("(No se imprimen porque las cadenas fueron rechazadas)")

# Ejecutar el programa
if __name__ == "__main__":
    main()




