#include<iostream>

using namespace std;

int dp[31][31] ={0,};

int dfs(int y, int x){
    if(x == 1 || x == y){
        return 1;
    }
    if(dp[y][x] != 0){
        return dp[y][x];
    }
    int res = 0;
    res = dfs(y-1, x-1) + dfs(y-1, x);
    dp[y][x] = res;
    return dp[y][x];
}

int main(){
    int R;
    int C;
    int W;
    int cnt = -1;
    cin>>R>>C>>W;


    int answer = 0;
    for(int i = R; i < R+W; i++){
        cnt++;
        for(int j = C; j <= C+cnt; j++){
            answer += dfs(i, j);
        }
    }
    cout<<answer;
}