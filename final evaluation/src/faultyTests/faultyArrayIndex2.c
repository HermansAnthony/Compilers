//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests the index of arrays (check for bounds)
//  This will result in a runtime error : instruction chk: value out of range.
//  ********************************************
int main(){
  int b = 4;
  int a[3] = {1};
  int c = a[b];
  return 0;
}
