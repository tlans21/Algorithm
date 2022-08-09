#include<iostream>
#include<queue>

using namespace std;

int N;

int main(){
    priority_queue<long long> pq;

    cin>>N;

    for(int i = 0; i < N*N; i++){
        long long temp;
        cin>>temp;


        if(pq.size() > N){
            pq.pop();
        }
        pq.push(-temp);
    }
    pq.pop(); // pq안에 6개가 들어있는 상태로 for문을 끝내므로 빼줘야한다.

    cout<<-pq.top();

    return 0;
}