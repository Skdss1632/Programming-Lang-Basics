cmake_minimum_required(VERSION 3.22)
project(untitled C)

set(CMAKE_C_STANDARD 11)

add_executable(untitled "main/main.c"
        include/write_a_func_that_prints_namaste_if_user_is_indian_and_bonjour_if_user_is_french.h
        include/write_a_func_to_calculate_sum_of_all_the_elements_of_the_array.h
        include/program_to_count_all_the_duplicates_in_an_array.h
        include/program_to_find_the_greatest_num_from_the_given_array.h
        include/program_to_find_the_smallest_num_from_the_given_array.h


)
