//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests global variables
//  ********************************************
#include <stdio.h>
int a = 1;
char b = 'b';
float c = 16.007;

int main() {
  printf("Global variables:\n");
  printf("%i (should be 1)\n", a);
  printf("b has value:%c (should be b)\n", b);
  printf("c has value:%f (should be 16.007)\n", c);
  int a = 8;
  char b = 'K';
  float c = 100000.7895;
  printf("a has local value:%i (should be 8)\n",a);
  printf("b has local value:%c (should be K)\n",b);
  printf("c has local value:%f (should be 100000.7895)\n",c);
  return 0;
}
