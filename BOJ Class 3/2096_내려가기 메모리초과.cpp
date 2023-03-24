#include<iostream>
#define MAX 500000
using namespace std;


int dp[MAX][4] = {0};
int dp2[MAX][4] = {0};



int main(){
    int N;

    cin >> N;

    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= 3; j++){
        cin>>dp[i][j];
        }
    }


    for(int i = 1; i <= N; i++){
        for(int j = 1; j<=3; j++){
            if(j==1){
            dp[i][j] += max(dp[i-1][j], dp[i-1][j+1]);
            dp2[i][j] += min(dp[i-1][j], dp[i-1][j+1]);
            }
            if(j==2){
                dp[i][j] +=max((dp[i-1][j], dp[i-1][j+1]), dp[i-1][j-1]);
                dp2[i][j] +=min((dp[i-1][j], dp[i-1][j+1]), dp[i-1][j-1]);
            }
            if(j==3){
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j]);
                dp2[i][j] += min(dp[i-1][j-1], dp[i-1][j]);
            } 
        }
    }


    cout<<max((dp[N][1], dp[N][2]), dp[N][3])<<" ";
    cout<<min((dp2[N][1], dp2[N][2]), dp2[N][3]);

    return 0;
}