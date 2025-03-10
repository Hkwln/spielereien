#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

int binary_search(int arr[], int left, int right, int target){
    while (left <= right) {
        // Find the middle point
        int mid = left + (right - left) / 2;
        
        // If element is present at the middle itself
        if (arr[mid] == target)
            return mid;
        
        // If element is smaller than mid, search in left half
        if (arr[mid] > target)
            right = mid - 1;
        
        // Else search in right half
        else
            left = mid + 1;
    }
    
    // Element not present in array
    return -1;

}

int main(){
    int size = 15;
    int arr[15];
    int target, result;
    // Generate a sorted array of random numbers
    srand(time(NULL));
    arr[0] = rand() % 10;
    for (int i = 1; i < size; i++) {
        arr[i] = arr[i-1] + rand() % 5 + 1;  // Ensure it's sorted
    }
    //print the array
    printf("Sorted array:");
    for(int i= 0; i < size; i++){
        printf("%d", arr[i]);
    }
    printf("\n");
    // Get number to search for
    printf("Enter a number you want to search for");
    scanf("%d", &target);
    result = binary_search(arr, 0 ,size-1, target);
}