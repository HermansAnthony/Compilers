#include <stdio.h>

int main() {
  int a = 0;

  while(a<5){
    if (a == 3){
      printf("Got value %i for a\n", a);
      continue;
    }
    a++;
  }
  printf("Broke out of loop at value %i\n",a);
  return 0;
}
