#include <stdio.h>
float f(){
  float g = 1.5;
  float k = 2.0;
  return g*k;
}

int i(){
  return 5;
}

int main(){
  // int c = f();
  // float g = f();
  // i();
  // printf("%i\n", g);
  int a = 5+1*2;
  printf("%i\n", a);
  a = (5+1)*2;
  printf("%i\n", a);
  return 0;
}
