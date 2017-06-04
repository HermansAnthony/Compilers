//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests different scope variables
//  ********************************************
#include <stdio.h>

int glob = 0;

int func() {
    glob = 2;
    int glob = 0;
    return 0;
}

int main(){
    func();
    printf("Glob should be 2: %i\n", glob);
}
