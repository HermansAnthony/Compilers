//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests pointer values
//  ********************************************
#include <stdio.h>
int main(){
  int a = 4;
  printf("Before:%i %s\n", a,"(should be 4)");
  int* y = &a;
  *y = 5;
  printf("After:%i %s\n", a,"(should be 5)");
}
