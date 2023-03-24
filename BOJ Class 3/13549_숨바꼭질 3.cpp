#include <iostream>
#include <vector>
#include <functional>
#include <queue>

using namespace std;

bool visited[100001];


int BFS(int X, int K){
 
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
    q.push(make_pair(0, X));
    visited[X] = true;
    

    while(!q.empty()){
        int cur = q.top().second;
        int count = q.top().first;
        q.pop();
 
        if(cur == K){
            return count;
        }

        if(cur * 2 <= 100000 && !visited[cur * 2]){
            visited[cur * 2] = true;
            q.push(make_pair(count, cur * 2));
        }

        if(cur + 1 <= 100000 && !visited[cur + 1]){
            visited[cur+1] = true;
            q.push(make_pair(count + 1, cur + 1));
        }
        if(cur - 1 >= 0 && !visited[cur - 1]){
            visited[cur -1] = true;
            q.push(make_pair(count + 1, cur - 1));
        }
    }     
}


int main(void){
    int N;
    int K;
    cin>>N>>K;

    cout<<BFS(N, K)<<endl;
    return 0;
}
