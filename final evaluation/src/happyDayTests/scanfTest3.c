//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests scanf functionality
//  ********************************************
#include <stdio.h>
int main() {
  float a;
  scanf("Enter a float: %f\n", &a);
  printf("The float you entered is: %f\n", a);
  return 0;
}
