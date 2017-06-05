//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests pointer values
//  ********************************************
#include <stdio.h>
int main(){
  char a = 'a';
  printf("Before:%c %s\n", a,"(should be a)");
  char* y = &a;
  char** b = &y;
  *y = 'y';
  **b = 'b';
  printf("After:%c %s\n", a,"(should be b)");
}
