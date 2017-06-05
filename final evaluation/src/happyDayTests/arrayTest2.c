//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests the initialization of arrays and use of array indices
//  ********************************************
#include <stdio.h>
int main(){
  float a[5] = {1.5,2.4,3.0,4.5,5.89};
  int middleElement = 2;
  a[middleElement] = a[4] - a[0];
  printf("%f\n", a[middleElement]);
  return 1;
}
