#include <stdio.h>
int main(){
  int a = 4;
  printf("First %i\n", a);
  int* y = &a;
  *y = 5;
  printf("After %i\n", a);
}
