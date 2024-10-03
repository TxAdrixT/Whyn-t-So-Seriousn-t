import random

def mostrar_palabra_aleatoria():
    # Lista de palabras
    palabras = [
        "manzana", "banana", "cereza", "durazno", "kiwi",
        "naranja", "pera", "sandía", "uva", "mora",
        "ananas", "coco", "mango", "limón", "fresa"
    ]

    # Seleccionar una palabra aleatoria
    palabra_aleatoria = random.choice(palabras)
    print(f"Palabra aleatoria: {palabra_aleatoria}")

# Ejecutar la función
mostrar_palabra_aleatoria()
