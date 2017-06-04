//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests the initialization of arrays
//  Index 5 of array a is out of bounds => throw warning + end program
//  ********************************************

int main() {
  int a[5] = {1,2,3,4,5};
  a[5] = 2;
  return 0;
}
