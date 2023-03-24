#include<iostream>
#include<queue>
#include<stack>
using namespace std;

int main(){
    int N;
    int cnt = 1;
    cin>>N;
    stack<int> s;
    queue<int> q;
    int stackNum;
    for(int i = 0; i < N; i++){
        int num;
        cin>>num;
        q.push(num);
    }
    
    while(!q.empty()){
        if(cnt == q.front()){
            q.pop();
            cnt++;
        }else{
            if(!s.empty() && s.top() == cnt){
                s.pop();
                cnt++;
            }else{
                s.push(q.front());
                q.pop();
            }
        }
    }
    while(!s.empty()){
        if(s.top() != cnt){
            cout<<"Sad"<<'\n';
            return 0;
        }else{
            s.pop();
        }
        cnt++;
    }
    cout<<"Nice"<<'\n';
    return 0;
}