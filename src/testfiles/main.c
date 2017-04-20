void f(float a, float b){
    int c = a + b;
}

char g(){
    char c = 'Hello world!';
    return c;
}

/*
    Overall main function that tests all functionality
*/

int main (int argc, char *argv[]) {
  f(1.0, 2.5);
  print(g());

  int ref = 1;
  int* p = &ref;

}