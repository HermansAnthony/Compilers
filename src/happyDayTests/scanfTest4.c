//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests scanf functionality
//  ********************************************
#include <stdio.h>
int main() {
  char a;
  scanf("Enter a character: %c\n", &a);
  printf("The character you entered is: %c\n", a);
  return 0;
}
