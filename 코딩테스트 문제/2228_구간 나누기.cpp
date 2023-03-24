#include<iostream>

using namespace std;

int dp[102][102];
int arr[102];
int search(int n, int m){
    

    if(m==0){
        return 0;
    }

    if(n<=0){
        return -987654321;
    }


    if(dp[n][m] != -1){
        return dp[n][m];
    }

    int prefix = 0;
    dp[n][m] = search(n-1, m); 
    

    for(int i = n; i > 0; i--){
        prefix += arr[i];
        int tmp = search(i-2, m-1) + prefix;
        if(tmp > dp[n][m]){
            dp[n][m] = tmp;
        }
    }
    return dp[n][m];
}



int main(){
    
    int N;
    int M;

    cin>>N>>M;

    for(int i = 1; i <= N; i++){
        cin>>arr[i];
        for(int j = 1; j<= N/2; j++){
            dp[i][j] = -1;
        }
    }

    cout<<search(N, M)<<'\n';
    return 0;
}