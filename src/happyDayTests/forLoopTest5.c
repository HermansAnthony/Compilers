//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests a regular forloop (with assignment of iterator)
//  ********************************************
#include <stdio.h>
int main(){
  float returnValue = 10.0;
  for (int i=0;i>-5;i = i-1) {
    returnValue = returnValue + 0.01;}
  printf("Float %f (should be 10.05)\n", returnValue);
  return 0;
}
