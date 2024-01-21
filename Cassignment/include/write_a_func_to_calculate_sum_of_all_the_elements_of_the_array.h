//
// Created by 91707 on 9/27/2023.
//

#ifndef UNTITLED_WRITE_A_FUNC_TO_CALCULATE_SUM_OF_ALL_THE_ELEMENTS_OF_THE_ARRAY_H
#define UNTITLED_WRITE_A_FUNC_TO_CALCULATE_SUM_OF_ALL_THE_ELEMENTS_OF_THE_ARRAY_H
#include "stdio.h"

// Function to calculate the sum of elements in an array
void sumArray(int arr[], int n) {
    int sum = 0;

    for (int i = 0; i < n; i++) {
        sum += arr[i]; // Add the current element to the sum
    }
    printf("Sum of the elements in the array: %d\n", sum);


}
#endif //UNTITLED_WRITE_A_FUNC_TO_CALCULATE_SUM_OF_ALL_THE_ELEMENTS_OF_THE_ARRAY_H
