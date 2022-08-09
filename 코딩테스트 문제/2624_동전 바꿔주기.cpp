#include<iostream>
#include<algorithm>
using namespace std;


int dp[101][10001]={0,};


int main(){
    int T;
    int K;
    cin>>T;
    cin>>K;

    pair<int,int> p[101];
    

    for(int i = 1; i <= K; i++){
        int a;
        int b;
        cin>>a>>b;
        p[i] = {a, b};
    }
    sort(p+1, p+K+1);
    dp[0][0] = 1;
    
    for(int i = 1; i <= K; i++){
        for(int j = 0; j <= p[i].second; j++){
            for(int k = 0; k <= T; k++){
                if(j * p[i].first + k > T){
                    break;
                }
                dp[i][j * p[i].first + k] += dp[i-1][k];
            }
        }
    }
    cout<<dp[K][T];
}