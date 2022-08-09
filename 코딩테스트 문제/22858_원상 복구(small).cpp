#include<iostream>

using namespace std;



int main(){
    int N;
    int K;
    cin>>N>>K;
    int S[N+1];
    int P[N+1];
    int D[N+1];

    for(int i = 1; i <= N; i++){
        int temp;
        cin>>S[i];
    }

    for(int i = 1; i <= N; i++){
        cin>>D[i];
    }// D저장

    while(K--){
        for(int i = 1; i <= N; i++){
            P[D[i]] = S[i];
        }
        for(int i = 1; i <= N; i++){
            S[i] = P[i];
        }
    }

    for(int i = 1; i <= N; i++){
        cout<<S[i]<<' ';
    }
    return 0;
}