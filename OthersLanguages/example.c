//#include <stdio.h>  Include the standar library

// int main() { // La función main inicia la ejecución del programa
//     printf("Hello World\n"); // Imprime "Hello, World!" seguido de un salto de línea
//     return 0; // Termina la ejecución del programa con estado de salida 0
// }

//It can not have two mains
int main() {
    // Variables declaration
    int num1, num2, suma;
    
    // Pedir al usuario que ingrese dos números
    printf("Enter the first number: ");
    scanf("%d", &num1);
    printf("Enter the second number: ");
    scanf("%d", &num2);
    
    // Calculate num1 + num2
    suma = num1 + num2;
    
    // Print the result
    printf("La suma de %d y %d es %d.\n", num1, num2, suma);
    
    // Verificar si la suma es par o impar usando el operador módulo (%)
    if (suma % 2 == 0) {
        printf("La suma es un número par.\n");
    } else {
        printf("La suma es un número impar.\n");
    }
    return 0;
}
