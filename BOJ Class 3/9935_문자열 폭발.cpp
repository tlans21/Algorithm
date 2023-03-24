#include<iostream>

using namespace std;

int main(){
    int N;
    int M;
    int map[1001][1001];
    cin>>N>>M;

    for(int i = 1; i <= N-1; i++){
        int x;
        int y;
        int z;  
        cin>>x>>y>>z;
        map[x][y] = z;
        map[y][x] = z;
    }

    for(int i = 0; i < M; i++){
        int a;
        int b;
        cin>>a>>b;
        cout<<map[a][b]<<'\n';
    }

}