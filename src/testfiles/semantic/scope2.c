#include <stdio.h>

int glob = 0;

int func(int glob) {
    glob = 2;
    int glob = 1;
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
    func();
    printf("Glob should be 2: %i\n", glob);
}
