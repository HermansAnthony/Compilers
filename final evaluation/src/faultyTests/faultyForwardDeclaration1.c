//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests forward declarations
//  f is forwardly declared with 2 parameters and not 1
//  ********************************************
int f(int a, float b);

int f(int a){
  return a;
}

int main(){
  return 0;
}
