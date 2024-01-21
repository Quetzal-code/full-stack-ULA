"""Baking calculator"""
EXPECTED_BAKE_TIME = 40
# Supongo que el tiempo de horneado esperado es de 60 minutos

def bake_time_remaining(elapsed_bake_time):
    """
    Calcula el tiempo de horneado restante.
    La función toma los minutos reales que la lasaña ha estado en el horno como
    argumento y devuelve cuántos minutos más necesita hornearse basándose en el
    'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

print(f"Tiempo de horneado restante: {bake_time_remaining(30)} minutos")

PREPARATION_TIME = 10

def preparation_time_in_minutes(number_of_layers):
    """
    Calcula el tiempo de preparación en minutos.
    
    :param layers: int - número de capas de la lasaña.
    :return: int - tiempo total de preparación (en minutos).
    """
    return PREPARATION_TIME * number_of_layers


print(f"Tiempo de horneado restante: {preparation_time_in_minutes(2)} minutos")


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calcula el tiempo total transcurrido en minutos.
    
    :param number_of_layers: int - número de capas de la lasaña.
    :param elapsed_bake_time: int - tiempo de horneado ya transcurrido.
    :return: int - tiempo total transcurrido (en minutos).
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

print(f"Tiempo de horneado restante: {elapsed_time_in_minutes(2, 30)} minutos")