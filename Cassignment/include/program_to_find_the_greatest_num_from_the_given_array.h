//
// Created by 91707 on 9/28/2023.
//

#pragma once
#include <stdio.h>

// Function to find the greatest number in an array
int findGreatest(int arr[], int size) {
    if (size == 0) {
        // Handle the case of an empty array
        printf("Array is empty.\n");
        return -1; // You can choose an appropriate value or error code
    }

    int greatest = arr[0]; // Assume the first element is the greatest

    for (int i = 1; i < size; i++) {
        if (arr[i] > greatest) {
            greatest = arr[i]; // Update greatest if a larger element is found
        }
    }

    return greatest;
}
