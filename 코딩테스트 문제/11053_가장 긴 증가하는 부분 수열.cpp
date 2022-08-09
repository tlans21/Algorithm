#include<iostream>

using namespace std;

int main(){
    int N;

    int arr[1001];
    int Max = 0;
    cin >> N;

    for(int i = 1; i <= N; i++){
        cin>>arr[i];
    }

    int dp[1001];
    
    for(int i = 1; i <= N; i++){
        dp[i] = 1;
        for(int j = 1; j<= N; j++){
            if(arr[i] > arr[j] && i>j){
                dp[i] = max(dp[j] + 1, dp[i]);
            }
        }
    }
    for(int i = 1; i <= N; i++){
        Max = max(Max, dp[i]); 
    }
    cout<<Max;
    return 0;
}