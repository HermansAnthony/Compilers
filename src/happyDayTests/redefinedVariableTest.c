//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests the working of the symbol table
//  Defined is a variable and a function
//  ********************************************
#include <stdio.h>
int defined(){
  return 2;
}

int main(){
  int defined = 0;
  for (int i =0; i< 5; i++){
    defined = defined + defined();
  }
  printf("Result: %i\n", defined);
  return defined;
}
