#include <stdio.h>

int main() {
    // Declare variables to store the three numbers
    double num1, num2, num3;

    // Prompt the user to enter the first number
    printf("Enter the first number: ");
    scanf("%lf", &num1);

    // Prompt the user to enter the second number
    printf("Enter the second number: ");
    scanf("%lf", &num2);

    // Prompt the user to enter the third number
    printf("Enter the third number: ");
    scanf("%lf", &num3);

    // Calculate the sum of the three numbers
    double sum = num1 + num2 + num3;

    // Display the result
    printf("The sum of %.2lf, %.2lf, and %.2lf is: %.2lf\n", num1, num2, num3, sum);

    return 0;
}
