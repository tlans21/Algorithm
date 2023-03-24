#include<iostream>

using namespace std;

int main(){
    int N;
    cin>>N;
    int map[N+1][N+1] ={0,};
    long long dp[N+1][N+1]={0,};
    
    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= N; j++){
            cin>>map[i][j];
        }
    }
    dp[1][1] = 1;

    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= N; j++){

            if(dp[i][j] == 0 || (i == N && j == N)){
                continue;
            }

            int loc = map[i][j];
            int right = loc + j;
            int down = loc + i;
            if(right <= N){ 
                dp[i][right] = dp[i][right] + dp[i][j];
            }
            if(down <= N){
                dp[down][j] = dp[down][j] + dp[i][j];
            }
        }
    }
    cout<<dp[N][N];
    return 0;
}