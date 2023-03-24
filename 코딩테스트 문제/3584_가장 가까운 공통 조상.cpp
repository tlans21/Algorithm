#include<iostream>


using namespace std;
int parent[10001];
bool visited[10001];

int T;
int N;
int u;
int v;
int s;
int k;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    cin>>T;

    for(int a = 0; a < T; a++){
        
        cin>>N;


        for(int i = 1; i <= N; i++){
            parent[i] = i;
            visited[i] = false;
        }
        for(int i = 0; i < N-1; i++){
            

            cin>>u>>v;
            parent[v] = u;
        }


      
        cin>>s>>k;

        visited[s] = true;
        while(s != parent[s]){
            s = parent[s];
            visited[s] = true;
        }
        while(1){
            if(visited[k] == true){
                cout<<k<<'\n';
                break;
            }
            k = parent[k];
        }
    }
}
