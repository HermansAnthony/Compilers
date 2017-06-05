//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests if a function has a return statement
//  If non void function has no return statement => print warning
//  ********************************************
float f1(){}
char f2(){}
int f3(){}
void f4(){}
float f5(){return 0.0;}

int main(){
  f1();
  f2();
  f3();
  f4();
  f5();
  return 0;
}
