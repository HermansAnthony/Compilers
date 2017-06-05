//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests scanf calls
//  More data arguments provided than flags present in the string constant
//  ********************************************
#include <stdio.h>

int main(){
  int a = 0;
  scanf("Hello %i\n", a, "semantic error");
}
