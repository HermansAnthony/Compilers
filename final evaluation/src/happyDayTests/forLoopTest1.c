//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests a regular forloop (with incrementing iterator)
//  ********************************************
#include <stdio.h>
int main(){
  int upperBound = 10;
  for (int iterator = 0; iterator < upperBound; iterator++){
    printf("This for loop is now at iteration %i\n", iterator);
  }
}
