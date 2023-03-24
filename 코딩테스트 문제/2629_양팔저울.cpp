#include<iostream>
using namespace std;

int N;
int M;
int W[30];
bool dp[31][15001]={0,};

void dfs(int cnt, int weight){
    if(cnt > N || dp[cnt][weight]){
        return;
    }
    dp[cnt][weight] = true;

    dfs(cnt + 1, weight + W[cnt]);
    dfs(cnt + 1, weight);
    dfs(cnt + 1, abs(weight - W[cnt]));
}

int main(void){
    cin>>N;
    for(int i = 0; i < N; i++){
        cin>>W[i];
    }
    dfs(0, 0);

    cin>>M;

    for(int i = 0; i < M; i++){
        int T;
        cin>>T;
        if(T> 15000){
            cout<<"N";
            continue;
        }
        if(dp[N][T] == true){
            cout<<"Y"<<' ';
        }else if(dp[N][T] == false){
            cout<<"N"<<' ';
        }
    }
    return 0;
}