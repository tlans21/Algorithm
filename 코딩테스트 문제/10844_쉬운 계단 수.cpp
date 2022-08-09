#include<iostream>

using namespace std;

int main(){
    int result;
    int N;
    cin>>N;
    int dp[101][10] = {0,};
    for(int i = 1; i <= 9; i++){
        dp[1][i] = 1;
    }

    for(int i = 2; i <= N; i++){
        for(int j = 0; j <= 9; j++){
            if(j == 0){
                dp[i][0] = dp[i-1][j+1] % 100000000;
            }else if(j == 9){
                dp[i][9] = dp[i-1][j-1] % 100000000;
            }else{
                dp[i][j] = (dp[i-1][j-1]%100000000  + dp[i-1][j+1]%100000000) % 100000000;
            }
        }
    }
    result = 0;

    for(int i = 0; i <= 9; i++){
        result = (result + dp[N][i]) % 100000000;
    }
    cout<<result;
    return 0;
}