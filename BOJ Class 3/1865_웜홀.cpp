#include<iostream>
#include<vector>
#define INF 10000000
using namespace std;
int N;
int M;
int dist[501];
vector<pair<int, int>> a[501];
bool Bellman_Ford(){
    for(int i = 0; i <= N; i++){
        dist[i] = INF;
    }
    dist[1] = 0;
    bool table = false;
    for(int i = 0; i <= N-1; i++){ // N번을 반복할 것
        for(int j = 1; j<=N; j++){ //N개의 노드를 확인
            for(int k = 0; k < a[j].size(); k++){ // 선택된 j의 간선
                int next = a[j][k].first;
                int weight = a[j][k].second;
                if(dist[next] > dist[j] + weight){//최소비용 갱신
                    dist[next] = dist[j] + weight;

                    if(i == N-1){
                        table = true; /*N-1번째 반복일때도 최소비용이 갱신된다면
                         음의 사이클을 가짐*/ 
                    }
                }
            }
        }
    }
    return table;
}

int main(){
    int Testcase;
    int W;
    int S;
    int E;
    int T;
    cin>>Testcase;
    for(int i = 0; i < Testcase; i++){
        cin>>N>>M>>W;
        
        for(int j = 0; j < M; j++){
            cin>>S>>E>>T;
            a[S].push_back({E, T});
            a[E].push_back({S, T});
        }

        for(int k = 0; k < W; k++){
            cin>>S>>E>>T;
            a[S].push_back({E, -T});
        }

        if(Bellman_Ford()){
            cout<<"YES"<<'\n';
        }else{
            cout<<"NO"<<'\n';
        }

        for(int i = 0; i <= N; i++){
            a[i].clear();
        }
    }
    return 0;
}