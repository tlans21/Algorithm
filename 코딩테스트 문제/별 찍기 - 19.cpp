#include<iostream>

using namespace std;

//4N-3  N =100일때 397이므로 넉넉하게 40
char map[400][400];

void check(int x, int y, int N){
    if(N == 1){
        map[x][y] = '*';
        return;
    }
    
    //위아래
    int len = 4*N - 3;
    for(int i = y; i < y+len; i++){
        map[x][i] = '*';
        map[x+len-1][i] = '*';
    }

    //양 옆
    for(int j = x; j < x+len; j++){
        map[j][y] = '*';
        map[j][y+len-1] = '*';
    }
    //새로운 사각형과 기존 사각형의 간격은 +2 만큼이다.

    check(x+2, y+2, N-1);
}

int main(){
    int N;

    cin>>N;
    for(int i = 0; i < 4*N-3; i++){
        for(int j = 0; j < 4*N - 3; j++){
            map[i][j] = ' ';
        }
    }

    check(0, 0, N);

    for(int i = 0; i < 4*N-3; i++){
        for(int j = 0; j < 4*N - 3; j++){
            cout<<map[i][j];
        }
        cout<<'\n';
    }
    return 0;
}