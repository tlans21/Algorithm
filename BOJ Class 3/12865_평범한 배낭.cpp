#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    int N;
    int K;
    int W;
    int V;
    int dp[101][100001] ={0};
    int maxi = 0;
    cin>>N>>K;
    for(int i = 1; i <= N; i++){
        cin>>W>>V;
        for(int j = 1; j <= K; j++){
              dp[i][j] = max(dp[i][j], dp[i-1][j]);
              if(j>=W){
                dp[i][j] = max(dp[i][j], dp[i-1][j-W]+V);
                maxi = max(maxi, dp[i][j]);
            }
        }
    }
    cout<<maxi;

    return 0;
}