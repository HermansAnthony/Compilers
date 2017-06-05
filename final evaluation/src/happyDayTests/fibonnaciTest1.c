//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This program will give you the fibonnaci series (recursive) with a specified input
//  ********************************************
#include <stdio.h>
int fib(int n){
  if (n == 0) {
    return 0;
  }
  if (n == 1) {
    return 1;
  }
  return fib(n - 1) + fib(n - 2);
}

int main(){
  int n = 0;
  printf("Give a value for n\n");
  scanf("%i", &n);
  printf("The fibonnaci series\n");
  for (int i = 0; i<=n; i++){
    int tempValue = fib(i);
    printf("%i\n", tempValue);
  }
}
