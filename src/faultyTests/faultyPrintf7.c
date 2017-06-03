//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests faulty printf calls
//  Redeclaration of printf is not supported
//  ********************************************
int printf(){
  return 0;
}

int main() {
  printf("1234");
  return 0;
}
