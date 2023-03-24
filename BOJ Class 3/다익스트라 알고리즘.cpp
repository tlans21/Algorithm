#include<iostream>
#define INF 12002303
using namespace std;
int Dist[100];
int MAP[101][101];
bool select[101];
int V;
int start;

int FindShorNode(){
    int Min_Dist = INF;
    int Min_Idx = -1;

    for(int i = 1; i <= V; i++){
        if(select[i] == true){
            continue;
        }
        if(Dist[i] < Min_Dist){
            Min_Dist = Dist[i];
            Min_Idx = i;
        }
    }
    return Min_Idx;
}
void Update_Dist(int NewNode){
    for(int i = 1; i <= V; i++){
        if(select[i] == true){
            continue;
        }
        if(Dist[i] > Dist[NewNode] + MAP[NewNode][i]){
            Dist[i] = Dist[NewNode] + MAP[NewNode][i];
        }
    }
}

int dijkstra(){
    for(int i = 1; i <=V; i++){
        Dist[i] = MAP[start][i];
        Dist[start] = 0;
        select[start] = true;
    for(int i = 0; i < V-1; i++){
        int NewNode = FindShorNode();
        select[NewNode] = true;
        Update_Dist(NewNode);
    }
    }
}