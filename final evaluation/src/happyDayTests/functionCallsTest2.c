//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This program tests function calls
//  ********************************************
#include <stdio.h>
float getFloat2(){
  return 5.12;
}

float getFloat(){
  return getFloat2() + 1.01;
}

int main(){
  float f = getFloat();
  printf("The float value: %f (should be 6.13)\n", f);
}
