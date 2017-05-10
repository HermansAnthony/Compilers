int defined(){
  return 2;
}

int main(){
  int defined = 0;
  for (int i =0; i< 5; i++){
    defined = defined + defined();
  }
  return defined;
}
