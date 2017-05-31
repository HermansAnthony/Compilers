//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests a forloop (with if else)
//  ********************************************
#include <stdio.h>
int main(){
  int iterator = 0;
  while(iterator < 10){
    printf("This loop is now at iteration %i\n", iterator);
    if (iterator == 5){
      printf("Loop ends at the iteration %i (should be 5)\n",iterator);
      break;
    }else{
      iterator++;
      continue;
    }
    printf("I should never reach this point\n");
  }
  printf("Loop ended\n");
}
