#include <stdio.h>

int a = 5;
int* f(){return &a;}
int main(){
  printf("%i\n", a);
  int* b = f();
  *b = 42;
  // printf("%i\n", a);
}
