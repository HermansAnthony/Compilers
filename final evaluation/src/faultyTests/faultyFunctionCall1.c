//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests function calls
//  F expects an integer and a char 
//  ********************************************

int f(int k, char c){
  k  = k + 1;
  c = '5';
  return k;
}

int main(){
  char a = '1';
  f('c', a);
  return 0;
}
