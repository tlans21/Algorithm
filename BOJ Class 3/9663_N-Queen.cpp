        #include<iostream>

        using namespace std;
        int N;
        int solution = 0;
        int row[15];

        bool check(int level){
            for(int i = 0; i < level; i++){
                if(row[i] == row[level] || abs(row[level] - row[i]) == (level - i)){
                    return false;
                }
            }
            return true;
        }
        void nqueen(int cnt){
            if(cnt == N){
                solution++;
            }else{
                for(int i = 0; i < N; i++){
                    row[cnt] = i;
                    if(check(cnt)){
                        nqueen(cnt + 1);
                    }
                }
            }
        }

        int main(){
            cin>>N;
            nqueen(0);
            cout<<solution;
            return 0;
        }