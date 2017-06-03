//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This program tests forward declarations
//  ********************************************
#include <stdio.h>
char f1();
char f2();

char f(){
  return f1();
}

char f1(){
  return f2();
}

char f2(){
  return 'Y';
}

int main(){
  char k = f();
  printf("Character: %c(should be Y)\n", k);
  return 0;
}
