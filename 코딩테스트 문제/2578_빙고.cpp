#include<iostream>

using namespace std;

int binggo[5][5];

bool find(){
    int cnt = 0;
    int crossR = 0;
    int crossL = 0;
    for(int i = 0; i < 5; i++){
        int row = 0;
        int column = 0;
        for(int j = 0; j < 5; j++){
            if(binggo[i][j] == 0){
                row++;
            }
            if(binggo[j][i] == 0){
                column++;
            }
        }
        if(row == 5){
            cnt++;
        }
        if(column == 5){
            cnt++;
        }
        if(binggo[i][i] == 0){
            crossR++;
        }
        if(binggo[i][4-i] == 0){
            crossL++;
        }
    }
    
    if(crossR == 5){
        cnt++;
    }
    if(crossL == 5){
        cnt++;
    }
    if(cnt >= 3){
        return true;
    }
    return false;
}


int main(){
    int count = 0;

    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){
            cin>>binggo[i][j];
        }
    }

    for(int i = 0; i < 25; i++){
        int num;
        cin>>num;
        for(int j = 0; j < 5; j++){
            for(int k = 0; k < 5; k++){    
                if(binggo[j][k] == num){
                    count++;
                    binggo[j][k] = 0;
                    if(i>10){
                        if(find()){
                            cout<<count;
                            return 0;
                        }
                    }
                }
            }
        }
    }
    return 0;
}
