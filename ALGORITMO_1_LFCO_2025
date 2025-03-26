import random
import time

# Función para generar cadenas válidas (S -> aSb | ε)
def generar_cadena_valida(cadenas_generadas):
    """
    Genera una cadena válida según la gramática S -> aSb | ε,
    asegurando que no se repitan valores.
    """
    opciones = ["ab", "aabb", "aaaabbbb"]
    for opcion in opciones:
        if opcion not in cadenas_generadas:
            cadenas_generadas.add(opcion)
            return opcion
    return ""  # En caso improbable de que todas ya estén presentes

# Función para generar cadenas inválidas
def generar_cadena_invalida(cadenas_generadas):
    """
    Genera una cadena que no sigue la gramática definida,
    evitando repeticiones.
    """
    opciones = ["aabaab", "baaabbaaa", "aaabaabbb"]
    for opcion in opciones:
        if opcion not in cadenas_generadas:
            cadenas_generadas.add(opcion)
            return opcion
    return ""  # En caso improbable de que todas ya estén presentes

# Función principal para mostrar las cadenas
def main():
    random.seed(time.time())  # Cambia la semilla en cada ejecución
    
    cadenas_validas_generadas = set()
    cadenas_invalidas_generadas = set()
    
    cadenas_validas = [generar_cadena_valida(cadenas_validas_generadas) for _ in range(3)]
    cadenas_invalidas = [generar_cadena_invalida(cadenas_invalidas_generadas) for _ in range(3)]

    print("Cadenas válidas:")
    for cadena in cadenas_validas:
        print(f"Cadena: '{cadena}'")
    
    print("\nCadenas inválidas:")
    for cadena in cadenas_invalidas:
        print(f"Cadena: '{cadena}'")

# Ejecutar el programa
if __name__ == "__main__":
    main()
