#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

bool visited[10001];
bool visited2[10001][9];
vector<int> a;
int arr[9];
int N;
int M;

void combination(int idx, int cnt){
    if(M == cnt){
        for(int i = 0; i < M; i++){   
            cout<<a[i]<<' ';
        }
        cout<<'\n';
        return;
    }
    for(int i = idx; i < N; i++){
        if(visited2[arr[i]][cnt] == true){
            continue;
        }
        
        visited2[arr[i]][cnt] = true;
        a.push_back(arr[i]);
        combination(i, cnt + 1);
        visited[i] = false;
        a.pop_back();
    }
    for(int i = 0; i < N; i++){
        visited2[arr[i]][cnt] = false;
    }
}

int main(){
     ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);


    cin>> N >> M;
    for(int i = 0 ; i < N; i++){ 
        cin>>arr[i];     
    }
    sort(arr, arr + N);
    combination(0, 0);
}