//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests a regular forloop (with incrementing iterator)
//  ********************************************
#include <stdio.h>
int main(){
  int upperBound = 10;
  for (int iterator = 0; iterator < upperBound; iterator++){
    printf("This for loop is now at iteration %i\n", iterator);
    if (iterator == 5){
      printf("Loop ends at the iteration %d\n",iterator);
      break;
    }else{
      continue;
    }
    printf("I should never reach this point\n");
  }
  printf("Loop ended\n");
}
