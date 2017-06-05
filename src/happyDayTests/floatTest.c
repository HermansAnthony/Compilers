#include <stdio.h>
int main(){
  float a = 12.69;
  // a++;
  float* b = &a;
  *b = 12.69-6;
  printf("%f\n",a );
}
