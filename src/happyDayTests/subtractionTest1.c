//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests subtraction of given values
//  ********************************************
#include <stdio.h>
int main(){
  int a;
  int b;
  printf("Give a number(integer):\n");
  scanf("%i", &a);
  printf("Give a second number(integer):\n");
  scanf("%i", &b);
  int y = a-b;
  printf("The subtraction results in value: %i \n",y);
}
