//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests if the argument has the same type as the parameter
//  ********************************************

void f(int a){
  a = a+1;
}

int main(){
  int a[5] = {1,2,3,4,5};
  f(a);
}
