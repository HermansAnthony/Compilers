//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests that dynamic arrays are not supported by our grammar
//  There is an expression which determines the array size (5-3)
//  ********************************************

int main(){
  int a[5-3];
  return 0;
}
