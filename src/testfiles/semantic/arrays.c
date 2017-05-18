int glob[5];

int main() {
    int x = 7;
    int y = 8;
    int z = 9;
    int *a[5] = {&x,&y,&z};
    int *b = a[2];
    return 0;    
}
