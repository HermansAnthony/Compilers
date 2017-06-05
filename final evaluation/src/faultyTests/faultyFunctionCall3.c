//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests function calls
//  F expects an array of integers and not char
//  ********************************************
int f(int a[5]){
  return 0;
}

int main(){
  char c[3] = {'a','b','c'};
  f(c);
  return 0;
}
