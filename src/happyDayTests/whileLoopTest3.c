//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests a while loop with a nested while loop
//  ********************************************
#include <stdio.h>
int main(){
  int i = 0;
  while (i<10){
    int j = 0;
    while(j<5){
      printf("First loop iterator: %i\n", i);
      printf("Second loop iterator: %i\n", j);
      j++;
    }
    i++;
  }
}
