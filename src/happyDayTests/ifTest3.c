//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests if two given values are the same
//  ********************************************
#include <stdio.h>
void compareIntegers(int a, int b){
  if (a == b){
    printf("The given integers are the same\n");
  }
  if (a != b){
    printf("The given integers are not the same\n");
  }
}

void compareFloats(float a, float b){
  if (a == b){
    printf("The given floats are the same\n");
  }
  if (a != b){
    printf("The given floats are not the same\n");
  }
}

void compareCharacters(char a, char b){
  if (a == b){
    printf("The given characters are the same\n");
  }else{
    printf("The given characters are not the same\n");
  }
}

int main(){
  char i;
  printf("Press i for integer comparison, f for float comparison and c for character comparison:\n");
  scanf("%c", &i);
  if (i == 'c'){
    char a;
    char b;
    scanf("First character: %c",&a);
    scanf("Second character: %c",&b);
    compareCharacters(a,b);
  }
  if (i == 'i'){
    int a;
    int b;
    scanf("First integer: %i",&a);
    scanf("Second integer: %i",&b);
    compareIntegers(a,b);
  }
  if (i == 'f'){
    float a;
    float b;
    scanf("First float: %f",&a);
    scanf("Second float: %f",&b);
    compareFloats(a,b);
  }
}
