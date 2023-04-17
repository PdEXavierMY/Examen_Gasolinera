import string
import sys


def solicitar_introducir_cadena(invite):
    """
    Esta función verifica que hay un dato introducido
    de al menos un carácter
    """
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        print(invite, end=": ")
        datoIntroducido = input()

        if len(datoIntroducido) > 0:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido
        else:
            print("¡¡La cadena introducida debe tener al menos 1 elemento!!")


def solicitar_introducir_char(invite):
    """
    Esta función verifica que hay un dato introducido de un carácter
    """
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        print(invite, end=": ")
        datoIntroducido = input()

        if len(datoIntroducido) == 0:
            # No se ha introducido nada
            print("Al menos debe indicar un carácter.", file=sys.stderr)
        elif len(datoIntroducido) > 1:
            # No se ha introducido nada 
            print("Debe indicar un único carácter.", file=sys.stderr)
        else:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido


def solicitar_introducir_letra(invite):
    """
    Esta función verifica que hay un dato introducido de una letra
    """
    while True:
        # Entramos en un bucle infinito

        datoIntroducido = solicitar_introducir_char(invite)

        if datoIntroducido in string.ascii_lowercase:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido
        elif datoIntroducido in string.ascii_uppercase:
            
            return datoIntroducido.lower()
        else:
            print("Tiene que ser una letra!")


def solicitar_introducir_palabra(invite):
    """
    Esta función verifica que hay un dato introducido entendiendo solo letras
    """
    while True:
        # Entramos en un bucle infinito

        datoIntroducido = solicitar_introducir_cadena(invite)

        for caracter in datoIntroducido:
            if caracter not in string.ascii_letters:
                # Un carácter no es una letra, empezamos de nuevo el bucle
                print("Tiene que ser una palabra!")
                break
        else:
            # Todos los carácters se han probado y son letras.
            return datoIntroducido.lower()


def solicitar_introducir_casilla(invite):
    """
    Esta función verifica que hay un dato introducido entendiendo solo letras
    """
    while True:
        # Entramos en un bucle infinito

        datoIntroducido = solicitar_introducir_cadena(invite)

        if len(datoIntroducido) != 2:
            print("Debe indicar una letra y una cifra.",
                file=sys.stderr)
        elif datoIntroducido[0] not in string.ascii_letters:
            print("El primer carácter introducido debe ser una letra.",
                file=sys.stderr)
        elif datoIntroducido[1] not in string.digits:
            print("El segundo carácter introducido debe ser una cifra.",
                file=sys.stderr)
        else:
            # Todos los carácters se han probado y son letras.
            return datoIntroducido.upper()