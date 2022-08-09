#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int N;
    cin>>N;
    int arr[N+1] ={0,};
    int dp[N+1] ={0,};
    for(int i = 1; i <= N; i++){
        cin>>arr[i];
    }
    dp[0] = 0;
    dp[1] = arr[1];
    dp[2] = arr[1] + arr[2];

    for(int i = 3; i <= N; i++){
        dp[i] = max(max(dp[i-3] + arr[i]+arr[i-1], dp[i-2] + arr[i]), dp[i-1]);
    }
    cout<<dp[N];
}