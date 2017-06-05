//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests subtraction of given values
//  ********************************************
#include <stdio.h>
int main(){
  float a;
  float b;
  printf("Give a number(float):\n");
  scanf("%f\n", &a);
  printf("Give a second number(float):\n");
  scanf("%f\n", &b);
  float y = a-b;
  printf("The subtraction results in value: %i \n",y);
}
