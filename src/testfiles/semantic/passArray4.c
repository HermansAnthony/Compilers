char func(char *b[5]) {
    return *b[2];
}

int main() {
    char x = 'a';
    char y = 'b';
    char z = 'c';
    char *a[5] = {&x, &y, &z};
    char b = func(a);
    return 0;    
}
