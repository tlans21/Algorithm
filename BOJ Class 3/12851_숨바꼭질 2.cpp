#include<iostream>
#include<queue>

using namespace std;

queue<int> q;
bool visited[100001];
int N;
int K;
int A;
int first;
int cnt2;

int BFS(int X, int cnt){
 
    queue<pair<int,int>> q;

    q.push({X, cnt});
    while(!q.empty()){
        int cur = q.front().first;
        int count = q.front().second;
        q.pop();
        visited[cur] = true;  // 1 -> (1+1) = 2 -> (2*2) = 4인 경우와 (1*1) = 2 - > (2*2)= 4인 경우의 값이 같은 경우.

        if(first && cnt2 == count && K == cur){
            first++;
        }

        if(K == cur && first == 0){
            first++;
            cnt2 = count;          
        }
        if(cur + 1 <= 100000 && !visited[cur + 1]){
            q.push({cur+1, count+1});
        }
        if(cur - 1 >= 0 && !visited[cur - 1]){
            q.push({cur-1, count+1});
        }
        if(cur * 2 <= 100000 && !visited[2 * cur]){
            q.push({cur * 2, count + 1});
        }
        }
        return cnt2;
    }


int main(){
    cin>>N>>K;

    cout<<BFS(N, 0)<<endl;
    cout<<first;
}