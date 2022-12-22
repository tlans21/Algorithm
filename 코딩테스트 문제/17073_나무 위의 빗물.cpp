#include<iostream>
#include<vector>
#include<set>
using namespace std;


vector<int> vec[500001];
vector<int> u1;
vector<int> v1;

int main(){
    cout.precision(10);
    int N;
    double W;
    double cnt = 0;
    
    cin>>N>>W;

    for(int i = 0; i < N-1; i++){
        int u;
        int v;
        
        cin>>u>>v;
        vec[u].push_back(v);
        vec[v].push_back(u);
    }
    
    for(int i = 2; i <= N; i++){
       if(vec[i].size() == 1){
        cnt++;
       }
    }
    double answer = W/cnt;
    cout<<fixed<<answer;
}
