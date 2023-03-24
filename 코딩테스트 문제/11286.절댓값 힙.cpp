#include<iostream>
#include<queue>
#include<stdlib.h>

using namespace std;

int main(){

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    int N;

    cin>>N;
    for(int i = 0; i < N; i++){
        int temp;
        cin>>temp;
        if(temp){
            pq.push(make_pair(abs(temp), temp));
        }else if(!temp){
            if(pq.empty()){
                cout<<"0"<<'\n';
            }else{
                cout<<pq.top().second<<'\n';
                pq.pop();
            }
        }
    }
    return 0;
}