#include<iostream>
#include<cstring>
using namespace std;

int main(){
    int T;
    int N;
    int M;
    int arr[21];
    int dp[10001];
    cin>>T;
    while(T--){
        memset(dp, 0, sizeof(dp));
        cin>>N;
        for(int i = 1; i <= N; i++){
            cin>>arr[i];
        }
        cin>>M;
        dp[0] = 1;
        for(int i = 1; i <=N; i++){
            for(int j = arr[i]; j <= M; j++){
                dp[j] += dp[j - arr[i]]; 
            }
        }
        
        
        cout<<dp[M]<<'\n';
    }
    return 0;
}