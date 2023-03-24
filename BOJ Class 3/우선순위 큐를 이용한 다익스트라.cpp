#include<iostream>
#include<queue>
#include<vector>
#define INF 10000002
using namespace std;

int Dist[100];
vector<int, int> Vertex[101];
bool select[101];
int V;
int start;

void Dijkstra_Using_Heap(){
    priority_queue<pair<int, int>>PQ;
    PQ.push(make_pair(0, start));
    Dist[start] = 0;

    while(!PQ.empty()){
        int Cost = -PQ.top().first;
        int cur = PQ.top().second;
        PQ.pop();

        for(int i = 0; i < Vertex[cur].size(); i++){
            int Next = Vertex[cur][i].first;
            int nCost = Vertex[cur][i].second;

            if(Dist[Next] > Cost + nCost){
                Dist[Next] = Cost + nCost;
                PQ.push(make_pair(-Dist[Next], Next));
            }
        }
    }

    for(int i = 1; i <= V; i++){
        if(Dist[i] == INF){
            cout<<"INF"<<endl;
        }else{
            cout<<Dist[i]<<endl;
        }
    }
}