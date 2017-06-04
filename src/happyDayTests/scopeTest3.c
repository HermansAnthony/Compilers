//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests different scopes variables
//  ********************************************
#include <stdio.h>
int main(){
  int a = 0;
  if (a == 0){
    if (1 == 1){
      int b = 0;
      printf("Second if %i (should be 0)\n", a);
    }
    float a = 2.123;
    printf("%f (should be 2.123)\n", a);
  }else{
    printf("%s\n","not here" );
  }
  printf("%i (should be 0)\n", a);
}
