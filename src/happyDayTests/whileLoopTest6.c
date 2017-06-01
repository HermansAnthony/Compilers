//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests a while loop
//  ********************************************
#include <stdio.h>
int main() {
  int a = 0;
  while(a<5){
    if (a == 3){
      printf("Got value %i for a\n", a);
      break;
    }
    a++;
  }
  printf("Broke out of loop at value %i\n",a);
  return 0;
}
