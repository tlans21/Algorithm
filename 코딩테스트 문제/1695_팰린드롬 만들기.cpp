#include<iostream>
#include<algorithm>

using namespace std;

int dp[5001][5001];
int arr[5001];

int search(int start, int end){
    if(start>=end){
        return 0;
    }
    if(dp[start][end] != 0){
        return dp[start][end];
    }
    int ans = 845465456;
    if(arr[start] == arr[end]){
        ans = min(ans, search(start+1, end-1));
    }else{
        ans = min(search(start ,end-1) + 1 , search(start + 1, end) + 1);
    }

    return dp[start][end] = ans;
}

int main(){
    int N;
    cin>>N;
    for(int i = 1; i <= N; i++){
        cin>>arr[i];
    }

    cout<<search(1, N);
}
