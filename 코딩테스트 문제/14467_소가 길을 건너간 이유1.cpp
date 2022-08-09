#include<iostream>
#include<map>
using namespace std;

int main(){
    int N;
    int cnt = 0;
    int cow[11] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
    cin>>N;

    for(int i = 0; i < N; i++){
        int loc;
        int num;
        cin>>num>>loc;
        if(cow[num] == -1){
            cow[num] = loc;
        }else if(cow[num] != -1 && cow[num] != loc){
            
            cnt++;
        }
    }
    cout<<cnt;
    return 0;
}