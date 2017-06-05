//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This program will calculate the factorial of a given number (recursive)
//  ********************************************
#include <stdio.h>
int multiplyNumbers(int n){
  if (n >= 1){
    return n*multiplyNumbers(n-1);
  }
  return 1;
}

int main(){
    int n;
    printf("Enter a integer: ");
    scanf("%d", &n);
    if (n<0){
      printf("Factorial of negative number doesn't exist\n",n);
      return;
    }
    int fact = multiplyNumbers(n);
    printf("Factorial of %d = %d", n, fact);
    return 0;
}
