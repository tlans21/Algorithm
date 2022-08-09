#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int N;
    cin>>N;
    int arr[11]={0,};
    int dp[11]={0,};
    int ans = 0;

    for(int i = 1; i <= N; i++){
        cin>>arr[i];
    }

    //dp[b] = a b까지 부분수열의 최대합이 a

    for(int i = 1; i <= N; i++){
        for(int j = 1; j < i; j++){
            if(arr[i] > arr[j]){
                dp[i] = max(dp[i], dp[j]);
            }
        }
        dp[i] += arr[i];
        ans = max(ans, dp[i]);
    }


    cout<<ans;
    return 0;
}