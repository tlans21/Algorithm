#include<iostream>

using namespace std;

int N;
int M;
int T;
int N_cnt;
int answer;

int main(){

    cin >> T;
    for(int i = 0; i < T; i++){
        cin >> N >> M;
        N_cnt = 1;
        answer = 1;
        while(M != 0){
            answer *= M;
            M--;
            answer /= N_cnt;
            N_cnt++;
            if(N_cnt == N+1){
                break;
            }
        }
        cout<<answer<<endl;
    }

    return 0;

}