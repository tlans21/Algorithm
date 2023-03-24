#include<iostream>
#include<cmath>

using namespace std;

int main(){
    long long N;
    cin>>N;
    long long arr[100001];
    for(int i = 1; i <= N; i++){
        cin>>arr[i];
    }
    long long dp[100001];
    arr[0] = 0;
    dp[0] = 0;
    long long res = -1000000001;

    for(int i = 1; i <= N; i++){
        dp[i] = max(dp[i-1] + arr[i], arr[i]);
        if(dp[i] > res){
            res = dp[i];
        }
    }
    cout<<res;
    return 0;
}