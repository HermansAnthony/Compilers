char func(char b[5]) {
    return b[3];
}

int main() {
    char a[5] = {'a','b','c'};
    char b = func(a);
    return 0;    
}
