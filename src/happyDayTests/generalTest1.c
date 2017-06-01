//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests general things like function calls etc
//  ********************************************
#include <stdio.h>
float f(float a, float b){
    float c = a + b*1.5;
    return c;
}

char g(){
    char c = '!';
    return c;
}

int main () {
  float a = f(2.0,3.0);
  printf("Should be 6.5: %f\n", a);
  char c = g();
  printf("Should be !: %c\n", c);

}
