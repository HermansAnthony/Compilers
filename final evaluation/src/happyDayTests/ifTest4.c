//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile compares two given integers and prints the largest
//  ********************************************
#include <stdio.h>
int compareIntegers(int a, int b){
  if (a <= b){
    printf("%d is larger then %d \n", b, a);
    return 0;
  }
  printf("%d is larger then %d \n", a, b);
}

int main(){
  int a;
  int b;
  scanf("First integer: %i",&a);
  scanf("Second integer: %i",&b);
  compareIntegers(a,b);
}
