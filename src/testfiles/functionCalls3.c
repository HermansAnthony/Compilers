int getInteger(){
  return 5;
}

float getFloat(){
  return getInteger() + 1.01;
}

int main(){
  float f = getFloat();
}
