//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests a while loop (with nested ifs)
//  ********************************************
#include <stdio.h>
int main() {
  int a = 0;
  int b = 1;
  int z = 5;
  while(b==1){
    if(a == 5){
      int a = 0;
      if (a == 0){
        printf("%i %s\n", a, "(should be 0)");
      }
      printf("Gonna break out loop now\n");
      break;
    }
    printf("Iteration %i\n", a);
    a++;
  }
  printf("Broke out of loop at value %i%s\n",a, "(should be 5)");
  return 0;
}
