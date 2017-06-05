//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests a while loop
//  Double declaration of a
//  ********************************************
#include <stdio.h>
int main(){
  int a = 5;
  int k = 0;
  while ( k < 5){
    int a = 65;
    printf("Value of a: %i(should be 65)\n", a);
    k++;
  }
  printf("Value of a: %i(should be 5)\n", a);
}
