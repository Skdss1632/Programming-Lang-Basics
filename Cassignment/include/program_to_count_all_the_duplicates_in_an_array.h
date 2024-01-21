//
// Created by 91707 on 9/28/2023.
//

#ifndef UNTITLED_PROGRAM_TO_COUNT_ALL_THE_DUPLICATES_IN_AN_ARRAY_H
#define UNTITLED_PROGRAM_TO_COUNT_ALL_THE_DUPLICATES_IN_AN_ARRAY_H

void count_duplicate(int arr[], int n){
    int count=0;
    for(int i=0; i<n; i++){
        for(int j= i+1; j<n; j++){
            if (arr[i] == arr[j]){
                count += 1;
            }
        }
    }
    printf("total duplicates are present in array is: %d", count);
}

#endif //UNTITLED_PROGRAM_TO_COUNT_ALL_THE_DUPLICATES_IN_AN_ARRAY_H
