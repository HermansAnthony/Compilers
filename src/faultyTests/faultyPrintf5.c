//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests printf calls
//  Use of %f flag for an integer
//  ********************************************
#include <stdio.h>

int main(){
  int a = 0;
  int b = 3.5;
  printf("The integer %i, wrong type for integer %f\n", a, b);
}
