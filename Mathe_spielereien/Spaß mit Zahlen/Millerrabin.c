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
        int *arr = NULL; //create a array which has a dynamic size_t
        int createList(number){
            int temp = number-1
            int size = 0;
            while (temp %2 == 0){
                size++;
                arr = realloc(arr, size * sizeof(int));
                //arr.append()
                arr[i] = temp
                temp = temp/2;
                
            }
        }
        createList(number);
        int r = generate_random(1, 100);


    }
    else{
        return false;
    }
    
}

int main(){}
