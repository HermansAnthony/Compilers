//  ********************************************
//  Authors: Jeroen Verstraelen - Anthony Hermans
//  Description: This testfile tests different scopes variables
//  ********************************************
#include <stdio.h>

int glob = 0;

int func(int glob) {
    glob = 1;
    if ( glob == 1 ) {
        int glob = 3;
        printf("Glob should be 3: %i\n", glob);
    }
    else {
        printf("I should not be here.\n");
    }
    printf("Glob should be 1: %i\n", glob);
}

int main(){
    func(glob);
    printf("Glob should be 0: %i\n", glob);
    glob = 5;
    printf("Glob should be 5: %i\n", glob);
}
