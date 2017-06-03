//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests multiplication of given values
//  ********************************************
#include <stdio.h>
int main(){
  float a;
  float b;
  printf("Give a number(float):\n");
  scanf("%f", &a);
  printf("Give a second number(float):\n");
  scanf("%f", &b);
  float y = a*b;
  printf("The multiplication results in value: %i \n",y);
}
