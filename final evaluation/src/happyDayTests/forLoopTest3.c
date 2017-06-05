//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests a for loop with a nested for loop
//  ********************************************
#include <stdio.h>
int main(){
  for (int i=0;i<5;i++){
    for (int j=0;j<10;j++){
      printf("First loop iterator: %i\n", i);
      printf("Second loop iterator: %i\n", j);
    }
  }
}
