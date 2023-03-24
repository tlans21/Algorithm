#include<iostream>

using namespace std;

int a1 = 2;
int a2 = 3;
int a3;
int c;

void sum(int *a, int *b, int *c){
  *c = *a + *b;
}

int main(){
    cout<<a3<<endl;
    sum(&a1, &a2, &a3);
    cout<<a3;
}