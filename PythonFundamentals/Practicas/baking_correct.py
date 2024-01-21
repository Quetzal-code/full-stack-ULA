EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
def bake_time_remaining(actual_time):
    """
    Calculate the bake time remaining.
    """
    return EXPECTED_BAKE_TIME - actual_time
def preparation_time_in_minutes(layers):
    """Total cooking time."""  
    return layers * PREPARATION_TIME
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return elapsed cooking time.
    This function takes two numbers representing the number of layers & the time     
     already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """  
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time