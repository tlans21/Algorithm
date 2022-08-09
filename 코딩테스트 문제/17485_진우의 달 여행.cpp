#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    int N;
    int M;
    int map[1001][1001] = {0,};
    int dp[1001][1001][3] = {0,};
    int res = 1000001;

    cin>>N>>M;

    for(int i = 1; i <= N; i++){
        for(int j = 1; j<= M; j++){
            cin>>map[i][j];
        }
    }
    dp[0][0][0] = 0;
    dp[0][0][1] = 0;
    dp[0][0][2] = 0;

    for(int i = 1; i <= N; i++){
        for(int j = 1; j<=M; j++){
            if(j == 1){
                dp[i][j][1] = dp[i-1][j][2] + map[i][j];
                dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1]) + map[i][j];
            }else if(j == M){
                dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + map[i][j];
                dp[i][j][1] = dp[i-1][j][0] + map[i][j];
            }else{
                dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + map[i][j];
                dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + map[i][j];
                dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1]) + map[i][j]; 
            }
        }
    }
    for(int i = 1; i <= M; i++){
        for(int j = 0; j <= 2; j++){
            if(dp[N][i][j] != 0){
                res = min(dp[N][i][j], res);
            }
        }
    }

    cout<<res;
    return 0;
}