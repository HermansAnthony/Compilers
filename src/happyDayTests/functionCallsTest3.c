//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This program tests function calls
//  ********************************************
#include <stdio.h>
char getCharacter(){
  return 'A';
}

int main(){
  char c = getCharacter();
  printf("The character %c(should be A)\n", c);
}
