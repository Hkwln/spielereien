#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int generate_random(int min, int max){
    return min + rand() %(max - min +1);
}

bool Millerrabin(int number){
    if (number == 1){
        return true;
    }
    if (number == 2){
        return true;
    }
    if(number % 2 != 0){
        int *arr = NULL; // create an array with dynamic size
        
        int temp = number - 1;
        int size = 0;
        while (temp % 2 == 0) {
            size++;
            arr = realloc(arr, size * sizeof(int));
            if (arr == NULL) {
                fprintf(stderr, "Memory allocation failed\n");
                exit(EXIT_FAILURE);
            }
            arr[size - 1] = temp;
            temp = temp / 2;
        }

        // Process the array (example: print its contents)
        for (int i = 0; i < size; i++) {
            printf("arr[%d] = %d\n", i, arr[i]);
            
        }

        free(arr);
        arr = NULL;
        int r = generate_random(1, 100);

    }
    else{
        return false;
    }
    
}

int main(){
    Millerrabin(89);
    return 0;
}
