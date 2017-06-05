//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests dereference assignments (floats)
//  ********************************************
#include <stdio.h>
int main() {
    float a = 12.007;
    printf("Value of a before: %f (should be 12.007)\n", a);
    float *b = &a;
    float **c = &b;
    **c = 1.43;
    printf("Value of a after: %f (should be 1.43)\n", a);
}
