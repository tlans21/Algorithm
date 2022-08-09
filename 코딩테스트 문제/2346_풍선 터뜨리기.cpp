#include<iostream>
#include<deque>
using namespace std;

int main(){
    int N;
    deque<pair<int, int>>ballon;

    cin>>N;

    for(int i = 0; i < N; i++){
        int temp;
        cin>>temp;
        ballon.push_back({temp, i+1}); //처음 저장 값은 쪽지 값, 두 번째 저장 값은 풍선의 인덱스 
    }

    while(1){
        cout<<ballon.front().second<<" ";
        int cnt = ballon.front().first;
        ballon.pop_front();
        if(ballon.empty()){
            break;
        }
        if(cnt > 0){
            for(int i = 0; i < cnt-1; i++){
                ballon.push_back(ballon.front());
                ballon.pop_front();
            }
        }else{
            for(int i = cnt; i < 0; i++){
                ballon.push_front(ballon.back());
                ballon.pop_back();
            }
        }
    }
    return 0;       
}