#include<iostream>

using namespace std;
bool flag = true;
int arr[2001];
int dp[2001][2001];

int main(){
    int N;
    int M;
    cin>>N;
    
    for(int i = 1; i <= N; i++){
        cin>>arr[i];
    }
    

    
    for(int i = 1; i <= N; i++){
        dp[i][i] = 1;
        if(arr[i] == arr[i+1] && i != N){
            dp[i][i+1] = 1;
        }
    }

    for(int i = 2; i <= N-1; i++){
        for(int j = 1; j <=N; j++){
            if(arr[j] == arr[j+i] && dp[j+1][j+i-1] == 1){
                dp[j][j+i] = 1;
            }
        }
    }

    cin>>M;

    for(int i = 1; i<=M; i++){
        int S;
        int E;
        cin>>S>>E;
        cout<<dp[S][E]<<'\n';
    }
    return 0;
}