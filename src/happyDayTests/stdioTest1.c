//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests printf and scanf functionality
//  ********************************************
#include <stdio.h>

int main(){
  char str1[10];
  char str2[30];
  printf("Enter name(10 characters):");
  scanf("Your name: %s", str1);
  for( int x = 0; x < 10; x++ ){
    printf("%c\n", str1[x]);
  }
  // printf("Enter your last name(30 characters): ");
  // scanf("%s", str2);
  // printf("Entered Name: %s\n", str1);
  // int i = 0;
  // while (i < 10){
  //   printf("%c", str1[i]);
  //   i++;
  // }
  // printf("Entered lastname: %s\n", str2);
  // int i = 0;
  // while (i < 10){
  //   printf("%c", str1[i]);
  //   i++;
  // }
}
