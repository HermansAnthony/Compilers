//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests global pointers
//  ********************************************
#include <stdio.h>
int originalInteger = 16;
int* firstPtr = &originalInteger;
int** secondPtr = &firstPtr;

char originalCharacter = 'H';
char* firstPtrChar = &originalCharacter;
char** secondPtrChar = &firstPtrChar;

int main(){
  printf("Original integer %i\n", originalInteger);
  **secondPtr = 20;
  printf("Original integer after pointer change (should be 20): %i\n", originalInteger);
  printf("Original character %i\n", originalCharacter);
  **secondPtrChar = 'A';
  printf("Original integer after pointer change (should be A): %c\n", originalInteger);
}
