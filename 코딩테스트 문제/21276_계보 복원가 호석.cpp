#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<queue>

using namespace std;

map<string, int> m1;
map<int, string> m2;
int indegree[1001];
vector<int> graph[1001];
vector<string> root;
vector<int> childName[1001];

void topologySort(string s){
    queue<int> q;
    q.push(m1[s]);
    while(!q.empty()){
        int x = q.front();
        q.pop();
        for(int i = 0; i < graph[x].size(); i++){
            int next = graph[x][i];
            indegree[next]--;
            if(indegree[next]){
                continue;
            }
            childName[x].push_back(next);
            q.push(next);
        }
    }
}

int main(){
    int N;
    int M;

    cin>>N;

    for(int i = 0; i < N; i++){
        string str;
        cin>>str;
        m1[str] = i;
        m2[i] = str;
    }
    
    cin>>M;
    
    for(int i = 0; i < M; i++){
        string a;
        string b;
        cin>>a>>b;
        indegree[m1[a]]++; // 진입차수
        graph[m1[b]].push_back(m1[a]);
    }

    for(int i = 0; i < N; i++){
        if(!indegree[i]){
            root.push_back(m2[i]); // 진입차수가 없다면 이것은 조상
        }
    }

    sort(root.begin(), root.end()); //사전순을 위한 정렬
    for(auto a : root){
        topologySort(a);
    }
    cout<<root.size()<<'\n';
    for(auto a : root){
        cout<<a<<' ';
    }
    cout<<'\n';

    for(auto f : m1){
        cout<<f.first<<' '<<childName[f.second].size()<<' ';
        vector<string> v;
        for(auto next : childName[f.second]){
            v.push_back(m2[next]);
        }
        sort(v.begin(), v.end());
        for(auto l : v){
            cout<<l<<' ';
        }
        cout<<'\n';
    }
}