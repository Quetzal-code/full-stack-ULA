#include <stdio.h>  //Incluye la biblioteca estándar de entrada/salida

// int main() { // La función main inicia la ejecución del programa
//     printf("Hello World\n"); // Imprime "Hello, World!" seguido de un salto de línea
//     return 0; // Termina la ejecución del programa con estado de salida 0
// }

//No puedes tener dos main
int main() {
    // Declaración de variables
    int num1, num2, suma;
    
    // Pedir al usuario que ingrese dos números
    printf("Ingrese el primer número: ");
    scanf("%d", &num1);
    printf("Ingrese el segundo número: ");
    scanf("%d", &num2);
    
    // Calcular la suma de num1 y num2
    suma = num1 + num2;
    
    // Imprimir la suma
    printf("La suma de %d y %d es %d.\n", num1, num2, suma);
    
    // Verificar si la suma es par o impar usando el operador módulo (%)
    if (suma % 2 == 0) {
        printf("La suma es un número par.\n");
    } else {
        printf("La suma es un número impar.\n");
    }
    return 0;
}
