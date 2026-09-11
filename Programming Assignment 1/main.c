#include "conversion.h"
#include <stdio.h>

int main() {
    int num = 42;
    
    char *binaryStr = makeBinary(num);
    if (binaryStr == NULL) {
        fprintf(stderr, "Memory allocation failed!\n");
        return 1;
    }

    printf("Decimal: %d\n", num);
    printf("Binary:  %s\n", binaryStr);

    // Free the heap memory allocated by makeBinary
    free(binaryStr);

    int x;
    printf("Please enter a value in base 10\n");
    scanf("%d", &x);
    char var = 'A';
    printf("%d", var);
    return 0;
}