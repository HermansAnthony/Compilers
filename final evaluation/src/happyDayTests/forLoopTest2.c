//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests a regular forloop (with decrementing iterator)
//  ********************************************
#include <stdio.h>
int main(){
  for (int iterator = 10; iterator != -1; iterator--){
    printf("This for loop is now at iteration %i\n", iterator);
  }
}
