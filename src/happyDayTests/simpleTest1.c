//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests simple assignments
//  ********************************************
#include <stdio.h>
int main(){
  int i = 0;
  int i2 =i;
  i = -1;
  printf("Variable i should be -1: %i\n", i);
  printf("Variable i2 should be 0: %i\n", i2);
}
