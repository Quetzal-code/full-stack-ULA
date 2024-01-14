"""Baking calculator"""
EXPECTED_BAKE_TIME = 60
# Supongo que el tiempo de horneado esperado es de 60 minutos

def bake_time_remaining(elapsed_bake_time):
    """
    Calcula el tiempo de horneado restante.
    La función toma los minutos reales que la lasaña ha estado en el horno como
    argumento y devuelve cuántos minutos más necesita hornearse basándose en el
    'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

resultado = bake_time_remaining(30)
print(f"Tiempo de horneado restante: {resultado} minutos")


# def calcular_y_mostrar_tiempo_restante(elapsed_bake_time):
#     """
#     Calcula y muestra el tiempo de horneado restante.
#     """
#     resultado = EXPECTED_BAKE_TIME - elapsed_bake_time
#     print(f"Tiempo de horneado restante: {resultado} minutos")

# # Llamar a la función
# calcular_y_mostrar_tiempo_restante(30)




# def preparation_time_in_minutes(layers):
#     """
#     Calcula el tiempo de preparación en minutos.

#     :param layers: int - número de capas de la lasaña.
#     :return: int - tiempo total de preparación (en minutos).

#     Esta función toma el número de capas de lasaña y devuelve el tiempo total
#     de preparación, asumiendo un tiempo de preparación fijo por cada capa.
#     """
#     return layers * PREPARATION_TIME

# def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
#     """
#     Calcula el tiempo total transcurrido en minutos.

#     :param number_of_layers: int - número de capas de la lasaña.
#     :param elapsed_bake_time: int - tiempo de horneado ya transcurrido.
#     :return: int - tiempo total transcurrido (en minutos).

#     Esta función toma el número de capas de lasaña y el tiempo de horneado ya
#     transcurrido y devuelve el tiempo total transcurrido (preparación + horneado).
#     """
#     return preparation_time_in_minutes(3) + elapsed_bake_time


# def bake_printer():
#     return print (bake_time_remaining) 

# bake_printer