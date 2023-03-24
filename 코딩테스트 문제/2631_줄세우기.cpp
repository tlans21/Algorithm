#include<iostream>

using namespace std;

int main(){
    int N;
    cin>>N;
    int arr[201] = {0,};

    for(int i = 1; i <= N; i++){
        cin>>arr[i];
    }
    
    int dp[201] = {0,};
    int Max = 0;

    for(int i = 1; i <= N; i++){
        dp[i] = 1;
        for(int j = 1; j <= N; j++){
            if(arr[i] > arr[j] && i > j){
                dp[i] = max(dp[j] + 1, dp[i]);
            }
        }
    }
    for(int i = 1; i <= N; i++){
        Max = max(dp[i], Max); 
    }
        cout<<N-Max;
}