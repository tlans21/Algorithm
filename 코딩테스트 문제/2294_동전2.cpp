#include<iostream>
#include<algorithm>

#define INF 10001

using namespace std;

int main(){
    int N;
    int K;
    int coin[101];
    int dp[10001];
    dp[0] = 0;

    cin>>N>>K;
    for(int i = 1; i <= K; i++){
        dp[i] = 10001;
    }
    
    for(int i = 1; i <= N; i++){
        cin>>coin[i];    
    }

    for(int i = 1; i <= K; i++){
        for(int j = 1; j <= N; j++){
            if(i - coin[j] >= 0){
                dp[i] = min(dp[i-coin[j]] + 1, dp[i]);
            }
        }
    }
    if(dp[K] == 10001){
        cout<<-1;
    }else if(dp[K] != 10001){
        cout<<dp[K];
    }
   return 0;    
}