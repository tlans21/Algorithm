#include<iostream>

using namespace std;

 int prefixsum[1025][1025] ={0};
int dp[1025][1025];

int main(){
    int x1;
    int x2;
    int y1;
    int y2;
    int N;
    int M;


    cin >> N >> M;

    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= N; j++){
            cin >> prefixsum[i][j];
            dp[i][j] = dp[i-1][j] + dp[i][j-1] -dp[i-1][j-1] + prefixsum[i][j];
        }
    }

    
    for(int i = 0; i < M; i++){
        cin>>x1>>y1>>x2>>y2;
        cout<<dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1]<<'\n'; 
    }
    return 0;
}