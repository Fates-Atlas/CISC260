#include "conversion.h"

const char *makeBinary(int input) {
    char *output= malloc(33);
    if (!output) return NULL;

    for (double n=31.0; n>=0; n--) {
        if (input > (int)pow(2.0, n)) {
            strcat(output, "0");
        }
    }
    output[32] = '\0';
    return output;
}