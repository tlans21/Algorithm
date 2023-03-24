#include <iostream>
#include <string>
#include <vector>

using namespace std;

int dp[100][100];

int main(){
    int m;
    int n;

    dp[1][1] = 0;
    cin>>m>>n;
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
            if(i == 2 && j == 2){
                continue;
            }
            if(i == 1 && j == 1){
                continue;
            }
            if(i == 1){
                dp[i][j] += (dp[i][j-1] + 1); 
            }else if(j == 1){
                dp[i][j] += (dp[i-1][j] + 1);
            }else{
                dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] +1);
            }
        }
    }
    int minimum = dp[n][m];
    cout<<minimum;
    return 0;
}