//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests printf and scanf functionality
//  ********************************************
#include <stdio.h>

int main(){
  char str1[10];
  // char str2[30];
  // printf("Enter name: ");
  scanf("Your name: %c", str1);
  // printf("Enter your last name: ");
  // scanf("%s", str2);
  // printf("Entered Name: %s\n", str1);
  for(int i = 0; i < 10; i++) {
    printf("%c", str1[i]);
}
  // printf("Entered Website:%c", str2[0]);
  // return(0);
}
