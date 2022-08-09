#include<iostream>
#include<algorithm>

using namespace std;


int main(){
    int dp[1001] = {};
    int s[1001] = {};
    int N;


    int cnt;

    cin>>N;

    for(int i = 0; i < N; i++){
        cin>>s[i];
    }

    for(int i = 0; i < N; i++){
         dp[i] = 1;
         for(int j = 0; j < i; j++){
           if(s[i] > s[j]){
              dp[i] = max(dp[i], dp[j]+1);  
           }
        }
        cnt = max(dp[i], cnt);
    }
    cout<< cnt << endl;
    return 0;
}
