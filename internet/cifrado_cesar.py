def cifrado_cesar(texto, desplazamiento=3):
    """
    Encripta un texto usando el cifrado César.
    :param texto: Texto a encriptar
    :param desplazamiento: Número de posiciones a desplazar (por defecto 3)
    :return: Texto encriptado
    """
    resultado = ""
    for caracter in texto:
        if caracter.isupper():
            # Encriptar mayúsculas
            resultado += chr((ord(caracter) + desplazamiento - 65) % 26 + 65)
        elif caracter.islower():
            # Encriptar minúsculas
            resultado += chr((ord(caracter) + desplazamiento - 97) % 26 + 97)
        elif caracter.isdigit():
            # Encriptar números desplazando 1
            nuevo_num = (int(caracter) + 1) % 10
            resultado += str(nuevo_num)
        else:
            # Mantener otros caracteres igual
            resultado += caracter
    return resultado

def main():
    print("Programa de Encriptación")

    # Obtener entrada del usuario
    texto_original = input("Ingresa el texto a encriptar: ")
    desplazamiento = int(input("Ingresa el número de desplazamiento (1-25): ") or "3")

    # Encriptar el texto
    texto_encriptado = cifrado_cesar(texto_original, desplazamiento)

    # Mostrar resultados
    print("\nResultados:")
    print(f"Texto original: {texto_original}")
    print(f"Texto encriptado: {texto_encriptado}")

if __name__ == "__main__":
    main()