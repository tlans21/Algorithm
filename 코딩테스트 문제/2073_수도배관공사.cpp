#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;


int main(){
    int P;
    int D;
    int C;
    int L;
    int ans = 0;
    int dp[100001] ={0,};
    dp[0] = 1;
    cin>>D>>P;
    for(int i = 1; i <= P; i++){
        cin>>L>>C;
        for(int j = D; j >=L; j--){
            if(j-L == 0){
                dp[j] = max(dp[j], C);
            }else if(j-L >0){
                dp[j] = max(min(dp[j-L], C), dp[j]);
            }
        }
    }
    cout<<dp[D];
    return 0;
}