#include<iostream>

using namespace std;

int main(){
    int N;
    int K;
    cin>>N>>K;

    int arr[N+1]={0,};
    int dp[K+1]={0,};

    for(int i = 1; i <= N; i++){
        cin>>arr[i];
    }
    dp[0] = 1;

    for(int i = 1; i <= N; i++){
        for(int j = arr[i]; j <= K; j++){
            dp[j] +=dp[j-arr[i]];
        }
    }

    cout<<dp[K];
    return 0;
}