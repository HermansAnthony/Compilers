//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests scanf functionality
//  ********************************************
#include <stdio.h>
int main() {
  int a;
  scanf("Enter a integer: %i\n", &a);
  printf("The integer you entered is: %i\n", a);
  return 0;
}
