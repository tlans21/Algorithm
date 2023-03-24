#include<iostream>

using namespace std;

int mini = 100000000;

char BW[8][8] = {
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B'
};
    
char WB[8][8] = {
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W'
};

char board[51][51];

int checkWB(int x, int y){
    int cnt = 0;
    for(int i = 0; i < 8; i++){
        for(int j = 0; j < 8; j++){
            if(board[x+i][y+j] != WB[i][j]){
                cnt++;
            }
        }
    }
    return cnt;
}

int checkBW(int x, int y){
    int cnt1 = 0;
    for(int i = 0; i < 8; i++){
        for(int j = 0; j < 8; j++){
            if(board[x+i][y+j] != BW[i][j]){
                cnt1++;
            }
        }
    }
    return cnt1;
}

int main(){

    //1) 첫 번째 사각형이 W인 경우

    //2) 첫 번째 사각형이 B인 경우

    int N;
    int M;
    
    cin>>N>>M;
    

    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            cin>>board[i][j];
        }
    }

    
    int res = 0;
    /*
    int cnt = 0;
    int cnt1 = 0;
    
    */
    /*for(int i = 0; i < N-7; i++){
        for(int j = 0; j < M-7; j++){
            for(int s = 0; s < 8; s++){
                for(int k = 0; k < 8; s++){
                    if(board[i+s][j+k] != WB[s][k]){
                        cnt++;
                    }
                    if(board[i+s][j+k] != BW[s][k]){
                        cnt1++;
                    }
                }
            }

            res = min(cnt, cnt1);

            if(mini > res){
                mini = res;
            }

        }
    }

    cout<<mini;*/
    for(int i = 0; i < N-7; i++){
        for(int j = 0; j < M-7; j++){
            
            res = min(checkBW(i, j), checkWB(i, j));
            if(mini > res){
                mini = res;
            }       
        }
    }
    cout<<mini;
}