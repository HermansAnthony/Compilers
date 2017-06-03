//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This program tests simple increment / decrement function calls
//  ********************************************
#include <stdio.h>
int increment(int b){
  return b+1;
}

int decrement(int b){
  return b-1;
}

int main(){
  int a = increment(5);
  printf("The value for a: %d(should be 6)\n", a);
  a = increment(a);
  printf("The value for a after increment: %d(should be 7)\n", a);
  a = decrement(a);
  printf("The value for a after decrement: %d(should be 6)\n", a);
  return 0;
}
