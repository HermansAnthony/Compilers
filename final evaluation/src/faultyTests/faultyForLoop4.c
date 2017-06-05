//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests a forloop
//  Iterator is already declared so throw error
//  ********************************************
#include <stdio.h>
int main(){
  int upperBound = 10;
  int iterator = 0;
  for (int iterator = 0; iterator < upperBound; iterator++){
    printf("This for loop is now at iteration %i\n", iterator );
  }
}
