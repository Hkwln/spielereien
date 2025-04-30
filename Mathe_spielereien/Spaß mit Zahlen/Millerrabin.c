#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
/*
Millerrabin.c:23:28: error: passing argument 1 of ‘realloc’ makes pointer from integer without a cast [-Wint-conversion]
23 |             *arr = realloc(*arr, size * sizeof(int));
   |                            ^~~~
   |                            |
   |                            int
In file included from Millerrabin.c:2:
/usr/include/stdlib.h:683:29: note: expected ‘void *’ but argument is of type ‘int’
683 | extern void *realloc (void *__ptr, size_t __size)
   |                       ~~~~~~^~~~~
Millerrabin.c:23:18: error: assignment to ‘int’ from ‘void *’ makes integer from pointer without a cast [-Wint-conversion]
23 |             *arr = realloc(*arr, size * sizeof(int));
   |                  ^
Millerrabin.c:24:19: error: subscripted value is neither array nor pointer nor vector
24 |             (*arr)[size - 1] = temp;
*/
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
            *arr = realloc(*arr, size * sizeof(int));
            if (arr == NULL) {
                fprintf(stderr, "Memory allocation failed\n");
                exit(EXIT_FAILURE);
            }
            arr[size - 1] = temp;
            temp = temp / 2;
        }
        
        
        createList(number, &arr);
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
