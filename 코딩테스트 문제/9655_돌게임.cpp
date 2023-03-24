#include<iostream>

using namespace std;

int main(){
    int N;
    cin>>N;

    int dp[1001];
    dp[1] = 1;
    dp[2] = 0;
    dp[3] = 1;

    for(int i = 4; i <= N; i++){
        if(dp[i-3] == 1){
            dp[i] = 0;
        }else if(dp[i-3] == 0){
            dp[i] = 1;
        }
    }
    if(dp[N] == 1){
        cout<<"SK";
    }else{
        cout<<"CY";
    }
    return 0;    
}