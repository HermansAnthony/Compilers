//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests division of given values
//  ********************************************
#include <stdio.h>
int main(){
  float a;
  float b;
  printf("Give a number(float):\n");
  scanf("%f", &a);
  printf("Give a second number(float):\n");
  scanf("%f", &b);
  float y = a/b;
  printf("The division results in value: %f \n",y);
}
