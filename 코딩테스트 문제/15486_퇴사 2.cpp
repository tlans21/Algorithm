#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    int N;
    int answer;
    cin>>N;
    int T[N+1] = {0};
    int P[N+2] = {0};
    for(int i = 1; i <= N; i++){

        cin>>T[i]>>P[i];
        
    }
  
    int dp[N+2] = {0};
    int Max_money = 0;
    for(int i = 1; i <= N+1; i++){

        Max_money = max(Max_money, dp[i]);
        
        if(i+T[i] > N+1){
            continue;
        }
        dp[i+T[i]] = max(dp[i+T[i]], Max_money + P[i]);
        
    }
    
    cout<<Max_money;       
    return 0;
}