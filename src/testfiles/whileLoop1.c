#include <stdio.h>

int main() {
  int a = 0;
  int b = 1;
  int z = 5;
  while(b==1){
    // while (z != 0 ){
    //   if (z == 1){
    //     break;
    //   }
    //   printf("%i\n", z);
    //   z--;
    // }
    if(a == 5){
      int a = 0;
      if (a == 0){
        printf("%s\n", "A has value 0");
      }
      printf("In break condition\n");
      break;
    }
    printf("%i\n", a);
    a++;
  }
  printf("Broke out of loop at value %i\n",a);
  return 0;
}