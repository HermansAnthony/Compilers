//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This program tests the operator precedence
//  ********************************************
#include <stdio.h>
int main(){
  int x = 5;
  int y = 8;
  int z = 9;
  int w = ((x+y)-x*y+z)/3;
  int d = (x+y)-x*y+z/3;
  printf("The result: %i (should be -6)\n", w);
  printf("The result: %i (should be -24)\n", d);
}
