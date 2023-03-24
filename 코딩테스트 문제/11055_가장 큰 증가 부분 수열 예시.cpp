#include<iostream>
#include<cmath>
using namespace std;

int main(){
    int N;
    int res = 0;
    cin>>N;
    int arr[N+1];
    int dp[N+1];
    for(int i = 1; i <= N; i++){
        cin>>arr[i];
    }
    for(int i = 1; i <= N; i++){
        if(arr[i-1] < arr[i]){
            dp[i] = dp[i-1] + arr[i];
        }else if(arr[i-1] >= arr[i]){
            dp[i] = arr[i];
        }
        if(dp[i] > res){
            res = dp[i];
        }
    }
    cout<<res;
    return 0;

}