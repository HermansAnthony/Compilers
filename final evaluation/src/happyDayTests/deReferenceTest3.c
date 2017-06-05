//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests dereference assignments (characters)
//  ********************************************
#include <stdio.h>
int main() {
    char a = 'a';
    printf("Value of a before: %c (should be a)\n", a);
    char *b = &a;
    char **c = &b;
    **c = 'A';
    printf("Value of a after: %c (should be A)\n", a);
}
