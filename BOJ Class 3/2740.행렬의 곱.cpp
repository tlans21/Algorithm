#include<iostream>

using namespace std;
int N;
int M;
int K;
int mapA[101][101];
int mapB[101][101];
int res[101][101];
void solution(int n, int k, int m){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < k; j++){
            for(int s = 0; s < m; s++){
                res[i][j]+= mapA[i][s] * mapB[s][j];
            }
        }
    }
}
int main(){
    cin>>N>>M;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            cin>>mapA[i][j];
        }
    }

    cin>>M>>K;
    for(int i = 0; i < M; i++){
        for(int j = 0; j < K; j++){
            cin>>mapB[i][j];
        }
    }
    solution(N, K, M);

    for(int i = 0; i < N; i++){
        for(int j = 0; j < K; j++){
            cout<<res[i][j]<<" ";
        }
        cout<<'\n';
    }
    return 0;
}