#include<iostream>
#include<algorithm>

using namespace std;
int n;
int map[500][500];
int j = 0;
int MAX = 1000000000;
bool visited[100][100];
int dx[2] = {0, 1};
int solution = 0;

void dfs(int y, int x, int depth, int sum){
    
    if(depth == n){
       solution = max(sum, solution);
    }

    for(int i = 0; i < 2; i++){
            int ny = y+1;           //오른쪽과 왼쪽으로 가는 경우
            int nx = x + dx[i];

        if(ny < 0 || ny>=n || nx < 0 || nx>=n){
            continue;
        }
        dfs(ny, nx, depth+1, sum + map[ny][nx]);
    }
}

int main(){

    cin >> n;


    for(int i = 0; i < n; i++){
        for(int j = 0;  j <= i; j++){
            cin >> map[i][j];
        }
    }
    dfs(0, 0, 1, map[0][0]);

    cout<<solution<<endl;
 
}