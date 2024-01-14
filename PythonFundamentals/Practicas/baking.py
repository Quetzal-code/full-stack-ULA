EXPECTED_BAKE_TIME = 60
# Supongo que el tiempo de horneado esperado es de 60 minutos

# Tiempo de preparación por capa en minutos
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """
    Calcula el tiempo de horneado restante.

    :param elapsed_bake_time: int - tiempo de horneado ya transcurrido.
    :return: int - tiempo de horneado restante (en minutos).

    La función toma los minutos reales que la lasaña ha estado en el horno como
    argumento y devuelve cuántos minutos más necesita hornearse basándose en el
    'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(layers):
    """
    Calcula el tiempo de preparación en minutos.

    :param layers: int - número de capas de la lasaña.
    :return: int - tiempo total de preparación (en minutos).

    Esta función toma el número de capas de lasaña y devuelve el tiempo total
    de preparación, asumiendo un tiempo de preparación fijo por cada capa.
    """
    return layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calcula el tiempo total transcurrido en minutos.

    :param number_of_layers: int - número de capas de la lasaña.
    :param elapsed_bake_time: int - tiempo de horneado ya transcurrido.
    :return: int - tiempo total transcurrido (en minutos).

    Esta función toma el número de capas de lasaña y el tiempo de horneado ya
    transcurrido y devuelve el tiempo total transcurrido (preparación + horneado).
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time



# import lasagna
# lasagna.EXPECTED_BAKE_TIME

EXPECTED_BAKE_TIME = 60

from lasagna import bake_time_remaining
bake_time_remaining(10)

from lasagna import preparation_time_in_minutes
preparation_time_in_minutes(2)

from lasagna import  elapsed_time_in_minutes
elapsed_time_in_minutes(2)

def bake_time_remaining(elapsed_bake_time):
        """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return 
    

def elapsed_time_in_minutes():
        return 10

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """