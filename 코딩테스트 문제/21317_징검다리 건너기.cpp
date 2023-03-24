#include<iostream>

using namespace std;

int main(){
    int N;
    cin>>N;
    int jump[N+1] = {0,};
    int bigjump[N+1] = {0,};
    int dp[N+1] = {0,};
    for(int i = 1; i <= N; i++){
        cin>>jump[i]>>bigjump[i]; 
    }
    int K;
    cin>>K;

    for(int i = 5; i <= N; i++){
        dp[i] = dp[i-5]+ + jump[i-1];
    }
}