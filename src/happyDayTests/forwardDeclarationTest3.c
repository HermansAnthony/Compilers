//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This program tests forward declarations
//  ********************************************
#include <stdio.h>

float f1();

int main(){
  float k = f1();
  printf("Float value: %f(should be 0.007)\n", k);
  return 0;
}

float f1(){
  return 0.007;
}
