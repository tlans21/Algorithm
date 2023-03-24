#include<iostream>

using namespace std;
int N;
int arr[2001];
int dp[2001][2001];
int dfs(int left, int right, int cnt){
    if(left > right){
        return 0;
    }
    if(dp[left][right] != 0){
        return dp[left][right];
    }

    int res = 0;
    
    res = max(dfs(left + 1, right, cnt + 1) + arr[left] * cnt, dfs(left, right - 1, cnt +1) + arr[right] * cnt );

    return dp[left][right] = res;
}
int main(){
    int N;
    cin>>N;

    for(int i = 1; i <= N; i++){
        cin>>arr[i];
    }
    cout<<dfs(1, N, 1);
    return 0;
}