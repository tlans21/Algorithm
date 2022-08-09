#include<iostream>

using namespace std;

int main(){
    int N;
    int M;
    int start;
    int end;
    int value;
    int store[10][10];

    cin >> N >> M;

    for(int i = 0; i < M; i++){
        cin>>start>>end>>value;
        store[start][end] = value;
    }

}