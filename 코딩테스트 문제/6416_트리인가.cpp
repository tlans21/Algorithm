#include<iostream>
#include<vector>
#include<set>

using namespace std;

vector<int> tree[100001];
set<int> s;
int visit[100001];
int conn[100001];
int root;
bool flag;


void dfs(int val){
    for(int i = 0; i < tree[val].size(); i++){
        int next = tree[val][i];
        if(visit[next] > 0 || next == root){
            flag = false;
            break;
        }
        visit[next] = 1;
        dfs(next);
    }
}

void check(){
    //루트가 2개인 경우
    for(auto it = s.begin(); it != s.end(); it++){
        int val = conn[*it];
        if(val == 0){
            if(root == -1){
                root = *it; // 루트가 1개일 때, *it의 값으로 변경되고 2개일때 else 코드로 갑니다.
            }else{
                flag = false;
                break;
            }
        }
        else if(val > 1){
            flag = false; // 2개이상 부모를 둔 경우
            break; 
        }
    }
    //루트가 없는 경우
    if(root == -1){
        flag = false;
    }
}


int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int u;
    int v;
    int k = 0;
    while(1){
        k++;
        cin>>u>>v;
        if(u == -1 && v == -1){
            break;
        }else if(u == 0 && v == 0){
            cout<<"Case " << k << "is a tree.\n";
            continue;
        }
        for(auto it = s.begin(); it != s.end(); it++){
            visit[*it] = 0;
            conn[*it] = 0;
            tree[*it].clear();
        }
        s.clear();
        flag = true;
        root = -1;

        s.insert(v);
        s.insert(u);
        tree[u].push_back(v);
        conn[v]++;
        while(1){
            cin>>u>>v;
            if(u == 0 && v == 0){
                break;
            }
            s.insert(u);
            s.insert(v);
            tree[u].push_back(v);
            conn[v]++;
        }
        check();
        if(flag){
            dfs(root);
            for(auto it = s.begin(); it != s.end(); it++){
                if(*it == root){
                    continue;
                }
                if(visit[*it] > 1){
                    flag = false;
                    break;
                }
            }
        }
        if(flag){
            cout<<"Case " << k <<" is a tree.\n";
        }else{
            cout<<"Case " << k <<" is not a tree.\n";
        }
    }
    return 0;
}