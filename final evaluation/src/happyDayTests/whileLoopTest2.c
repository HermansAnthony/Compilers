//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests a regular while loop (decrementing iterator)
//  ********************************************
#include <stdio.h>
int main(){
  int iterator = 10;
  while(iterator!=-1){
    printf("This while loop is now at iteration %i\n", iterator );
    iterator--;
  }
}
