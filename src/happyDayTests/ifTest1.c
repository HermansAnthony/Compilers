//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests if statement/condition
//  ********************************************
#include <stdio.h>
int main(){
  int a = 1;
  int b = 2;
  if (a == b){
    printf("I should not be in this statement\n");
    return 0;
  }else{
    printf("If condition is false.\n");
    return -1;
  }
}
