def abrir_muneca(tamaño):
    # Caso base: La muñeca más pequeña ya no tiene nada adentro
    if tamaño <= 1:
        print("¡Llegaste a la muñeca más pequeña! Ya no hay más.")
        return

    # Caso recursivo: Abres la muñeca actual y encuentras otra más chica
    print(f"Abriendo muñeca de tamaño {tamaño}...")
    abrir_muneca(tamaño - 1)  # La función se llama a sí misma


# Comenzamos con una muñeca de tamaño 4
abrir_muneca(100)
