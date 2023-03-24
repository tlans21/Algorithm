#include<iostream>
#include<queue>

using namespace std;

int main(){
    priority_queue<int> pq;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin>>N;
    for(int i = 0; i < N; i++){
        int temp;
        cin>>temp;
        if(temp){
            pq.push(temp);
        }else{
            if(pq.empty()){
                cout<<0<<'\n';
            }else{
                cout<<pq.top()<<'\n';
                pq.pop();
            }
        }
    }
return 0;
}