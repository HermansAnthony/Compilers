//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This program tests the operator precedence
//  ********************************************
#include <stdio.h>
int main(){
  int x = 5;
  int y = 8;
  int z = 9;
  int w = (x+y)-x*y+z;
  printf("The result: %i (should be -18)\n", w);
}
