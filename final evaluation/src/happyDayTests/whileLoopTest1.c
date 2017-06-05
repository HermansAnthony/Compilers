//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests a regular while loop
//  ********************************************
#include <stdio.h>
int main(){
  int upperBound = 10;
  int iterator = 0;
  while(iterator<upperBound){
    printf("This while loop is now at iteration %i\n", iterator );
    iterator++;
  }
}
