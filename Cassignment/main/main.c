//
// Created by 91707 on 8/30/2023.
//

#include "../include/write_2_func_one_to_print_hello_and_2nd_to_print_good_bye.h"
#include "../include/write_a_func_that_prints_namaste_if_user_is_indian_and_bonjour_if_user_is_french.h"
#include "../include/sum_of_two_numbers.h"
#include "../include/write_a_func_to_calculate_sum_of_all_the_elements_of_the_array.h"
#include "../include/program_to_count_all_the_duplicates_in_an_array.h"
#include "../include/program_to_find_the_greatest_num_from_the_given_array.h"
#include "../include/program_to_find_the_smallest_num_from_the_given_array.h"

int main() {
    int arr[] = {5, 2, 5};
    int size = sizeof(arr) / sizeof(arr[0]);

    int smallest = find_smallest(arr, size);

    if (smallest != -1) {
        printf("The greatest number in the array is: %d\n", smallest);
    }

    return 0;
}



