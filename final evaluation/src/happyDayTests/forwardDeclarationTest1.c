//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This program tests forward declarations
//  ********************************************
#include <stdio.h>
// forward declaration
int f();

int k(){
  return 5+f();
}

int f(){
  return 10;
}

int main(){
  int z = k();
  printf("Result: %i(should be 15)\n", z);
  return 0;
}
