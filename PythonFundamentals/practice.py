# prompt: realiza en codigo de la conjetura de la absorcion de los multiplos de 3 que convergen al numero 153
def conjetura_absorcion_multiplos_3(numero):
    """
    Implementa la conjetura de la absorción de los múltiplos de 3 que convergen a 153.
    Args:
        numero: Un número entero positivo.
    Returns:
        Una lista de números que representa la secuencia hasta llegar a 153, o None si no converge.
    """
    secuencia = [numero]
    while secuencia[-1] != 153 and secuencia[-1] > 153:
        suma_cubos = 0
        suma_cubos = sum(int(digito)**3 for digito in str(secuencia[-1]))
        if suma_cubos in secuencia:
            return None  # No converge
        secuencia.append(suma_cubos)

    if secuencia[-1] == 153:
        return secuencia
    else:
        return None
# Ejemplo de uso
numero_inicial = 369
resultado = conjetura_absorcion_multiplos_3(numero_inicial)

if resultado:
    print(f"La secuencia para {numero_inicial} es: {resultado}")
else:
    print(f"El número {numero_inicial} no converge a 153 según esta conjetura.")
