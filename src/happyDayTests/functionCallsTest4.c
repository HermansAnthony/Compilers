//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This program tests function calls
//  ********************************************
#include <stdio.h>
char g(char x){
  x = 'k';
  return x;
}

int main(){
  char c = g('z');
  printf("The character: %c(should be k)\n", c);
  return 0;
}
