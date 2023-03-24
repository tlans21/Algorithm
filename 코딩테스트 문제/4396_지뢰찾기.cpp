#include<iostream>


using namespace std;

int N;
char map[11][11];
char input[11][11];
char output[11][11];
bool boom = false;

int dx[8] = {-1, 1, 0, 0, -1, -1, 1, 1};
int dy[8] = {0, 0, 1, -1, 1, -1, 1, -1};


int check(int y, int x, int cnt){
    for(int i = 0; i < 8; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(nx < 0 || nx >= N || ny < 0 || ny >= N){
            continue;
        }

        if(map[ny][nx] == '*'){
            cnt++; 
        }
    }
    return cnt;
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin>>N;
    
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cin>>map[i][j];
        }
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cin>>input[i][j];
        }
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(input[i][j] == 'x'){
                //클릭할때 주위의 지뢰수 표기
                int cnt = check(i, j, 0);
                output[i][j] = cnt + '0';
                //클릭했는데 지뢰인 경우
                if(map[i][j] == '*'){
                    boom = true;
                    continue;
                    //후에 처리합니다.
                }
            }
            //클릭 안한 경우
            else if(input[i][j] == '.'){
                output[i][j] = '.';
            }
        }
    }
    //지뢰가 터졌다면 표시
    if(boom){
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(map[i][j] == '*'){
                    output[i][j] = '*';
                }
            }
        }
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cout<<output[i][j];
        }
        cout<<'\n';
    }
    return 0;
}
    