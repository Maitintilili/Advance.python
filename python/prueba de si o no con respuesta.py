def elegir_respuesta():
    respuesta = input("Elige 'si' o 'no': ")
    if respuesta.lower() == "si":
        print("Elegiste 'si'.")
    elif respuesta.lower() == "no":
        print("Elegiste 'no'.")
    else:
        print("Respuesta no válida.")

def main():
    elegir_respuesta()

if __name__ == "__main__":
    main()

