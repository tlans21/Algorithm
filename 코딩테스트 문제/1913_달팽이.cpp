#include<iostream>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int N;
    int question;
    cin>>N;
    cin>>question;
    int map[N][N];
    int tmp = N;
    int answer1;
    int answer2;
    

    int r = N/2;
    map[r][r] = 1;
    
    for(int i = 0; i < r; i++){
        for(int j = 0; j < tmp-1; j++){
                map[j+i][i] = tmp * tmp - j;
                map[N-1-i][j+i] = tmp * tmp-j-(tmp-1);
                map[N-1-i-j][N-1-i] = tmp*tmp-j-2*(tmp-1);
                map[i][N-1-j-i] = tmp*tmp-j-3*(tmp-1);


                if(question == map[j+i][i]){
                    answer1 = j+i;
                    answer2 = i;      
                }
                else if(question == map[N-1-i][j+i]){
                    answer1 = N-1-i;
                    answer2 = j+i;
                }
                else if(question == map[N-1-i-j][N-1-i]){
                    answer1 = N-1-i-j;
                    answer2 = N-1-i;
                }
                else if(question == map[i][N-1-j-i]){
                    answer1 = i;
                    answer2 = N-1-j-i;
                }
                if(question == 1){
                    answer1 = r;
                    answer2 = r;
                }
        }
        tmp = tmp - 2;
    }
    for(int i = 0 ; i < N; i++){
        for(int j = 0; j < N; j++){
            cout<<map[i][j]<<" ";
        }
        cout<<'\n';
    }
    cout<<answer1+1<<" "<<answer2+1;
    return 0;
}