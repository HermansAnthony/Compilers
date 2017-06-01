//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests scanf functionality
//  ********************************************
#include <stdio.h>
int main(){
   char character;
   char word[10];
   scanf("%c", &character);
   printf("Entered character is %c\n", character);
   printf("Enter any string (10 characters max)\n");
   scanf("%s", word);
   printf("Entered string is %s \n", word);
}
