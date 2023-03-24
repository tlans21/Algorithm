#include<iostream>

using namespace std;

long long dp[37] ={0};
int n;

long long dfs(int N){

    if(N == 0){
        return 1;
    }
    if(dp[N] != 0){
        return dp[N];
    }
    long long res = 0;
    for(int i = 0; i <= N-1; i++){
        res +=(dfs(i) * dfs(N-1-i));
    }
    dp[N] = res;
    return dp[N];
}
int main(){
    cin>>n;
    cout<<dfs(n);
}