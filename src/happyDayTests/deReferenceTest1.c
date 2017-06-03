//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests dereference assignments (integers)
//  ********************************************
#include <stdio.h>
int main() {
    int a = 5;
    printf("Value of a before: %i (should be 5)\n", a);
    int *b = &a;
    int **c = &b;
    **c = 4;
    printf("Value of a after: %i (should be 4)\n", a);
}
