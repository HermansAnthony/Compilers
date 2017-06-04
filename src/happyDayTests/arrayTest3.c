//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests the initialization of arrays and use of array indices
//
//  ********************************************
int glob[5];

int main() {
    int x = 7;
    int y = 8;
    int z = 9;
    int *a[5] = {&x,&y,&z};
    int *b = a[2];
    return 0;
}
