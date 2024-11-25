# Crear una función que reciba el número y nos devuelva la categoría

def cat_edad(numero):
    """
    Función para categorizar edades.

    Parámetros:
    - numero (int): Número que se va a categorizar.

    Retorna:
    - str: Categoría a la que pertenece la edad.
    """
    if 18<= numero <= 28:
        return 'Jóven adulto'
    if 29<= numero <= 39:
        return 'Adulto jóven'
    if 40<= numero <= 50:
        return 'Mediana edad'
    else:
        return 'Adulto mayor'

