#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

const int INF = 0x3f3f3f3f;

int N;
int M;
int arrN[501]={0};
int arrM[501]={0};
int dp[501][501];

int divideConquer(int start, int end){
    if(start == end){
        return dp[start][end] = 0;
    }
    if(dp[start][end] != INF){
        return dp[start][end];
    }

    for(int mid = start; mid < end; mid++){
        int left = divideConquer(start, mid);
        int right = divideConquer(mid + 1, end);
        int res = left + right + arrN[start] * arrM[mid] * arrM[end];
        dp[start][end] = min(res, dp[start][end]);
    }

    return dp[start][end];
}

int main(){
    
    cin>>N;
    memset(dp, 0x3f, sizeof(dp));
    for(int i = 1; i <= N; i++){
        cin>>arrN[i]>>arrM[i];
    }

    cout<<divideConquer(1, N);

    


    return 0;
}