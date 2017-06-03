//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile compares two given floats and prints the largest
//  ********************************************
#include <stdio.h>
int compareFloats(float a, float b){
  if (a <= b){
    printf("%f is larger then %f \n", b, a);
    return 0;
  }
  printf("%f is larger then %f \n", a, b);
}

int main(){
  float a;
  float b;
  scanf("First float: %f",&a);
  scanf("Second float: %f",&b);
  compareFloats(a,b);
}
