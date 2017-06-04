//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests the initialization of arrays and use of array indices
//  ********************************************
#include <stdio.h>
int main() {
    int x = 7;
    int y = 8;
    int z = 9;
    int *a[5] = {&x,&y,&z,&x,&y};
    int *b = a[2];
    printf("%i-%i-%i-%i-%i (should be 7-8-9-7-8)\n",*a[0],*a[1],*a[2],*a[3],*a[4]);
    printf("%i (should be 9)\n", *b);
    return 0;
}
