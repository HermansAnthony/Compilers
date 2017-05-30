//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests forward declarations
//  f has parameter of type int and not float
//  ********************************************
void f(int k);

void f(float k){}

int main(){
  return 0;
}
