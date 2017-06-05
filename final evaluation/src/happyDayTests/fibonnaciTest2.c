//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This program will give you the fibonnaci series (non recursive) with a specified input
//  ********************************************
#include <stdio.h>

int main(){
  int n = 0;
  printf("Give a value for n\n");
  scanf("%i", &n);
  int first = 0;
  int second = 1;
  int next = 0;
  printf("The %d first numbers of the fibonnaci series\n", n);
  for (int i = 0 ; i < n ; i++ ){
   if (i <= 1){
     next = i;
   }else{
      next = first + second;
      first = second;
      second = next;
   }
   printf("%d\n",next);
  }
  return 0;
}
