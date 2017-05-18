float func(int c[5], float d[5]) {
    return d[3];
}

int main() {
    int a[5] = {1,2,3};
    float b[5] = {1.0,2.0,3.0};
    float e = func(a,b) + 4.2;
    return 0;    
}
