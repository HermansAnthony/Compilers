//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests the initialization of arrays and use of array indices
//  ********************************************
#include <stdio.h>
int main(){
  int a[3] = {1,2,3};
  printf("Before: %i-%i-%i\n", a[0], a[1], a[2]);
  a[0] = 5;
  a[1] = 10;
  a[2] = 15;
  printf("After: %i-%i-%i\n", a[0], a[1], a[2]);
}
