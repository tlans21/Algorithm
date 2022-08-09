#include<iostream>
#include<vector>

using namespace std;
int N;
int K;
int root;
int leaf = 0;
vector<int> tree[51];

int dfs(int node){
    if(node == K){
        return -1;
    }
    if(!tree[node].size()){
        leaf++;
        return 0;
    }
    for(int i = 0; i < tree[node].size(); i++){
        int temp = dfs(tree[node][i]);
        if(temp == -1 && tree[node].size() == 1){
            leaf++;
        }
    }
    return 0;
}
int main(){
    int num;
    cin >> N;
    for(int i = 0; i < N; i++){
        cin>>num;
        if(num == -1){
            root = i;
        }else{
            tree[num].push_back(i);
        }
    }
    cin>>K;
    dfs(root);
    cout<<leaf;
    return 0;
}