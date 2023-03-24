#include<iostream>

using namespace std;


long long N;
long long B;
long temp[5][5];
long long A[5][5];
long long unit[5][5];

void metrix(long long A[5][5], long long B[5][5]){
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            temp[i][j] = 0; // 이전 곱셈을 통해 저장된 값을 초기화.
            for(int k = 0; k < N; k++){
                temp[i][j]+= (A[i][k] * B[k][j]);
                temp[i][j] %= 1000;
            } 
        }
    }
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            A[i][j] = temp[i][j];
        }
    }
}

int main(){
    cin>>N>>B;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cin>>A[i][j];
            unit[i][i] = 1;
        }
    }
    while(B>0){
        if(B % 2 == 1){
            metrix(unit, A);
        }
        metrix(A, A);
        B = B/2;
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cout<<unit[i][j]<<' ';
        }
        cout<<'\n';
    }    
}