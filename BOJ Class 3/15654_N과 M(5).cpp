#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

bool visited[9];
vector<int> a;
int arr[9];
int N;
int M;

void combination(int cnt){
    if(M == cnt){
        for(int i = 0; i < M; i++){   
            cout<<a[i]<<' ';
        }
        cout<<'\n';
        return;
    }
    for(int i = 0; i < N; i++){
        if(visited[i] == true){
            continue;
        }
        visited[i] = true;
        a.push_back(arr[i]);
        combination(cnt + 1);
        visited[i] = false;
        a.pop_back();
    }
}

int main(){
     ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);


    cin>> N >> M;
    for(int i = 0 ; i < N; i++){ 
        cin>>arr[i];     
    }
    sort(arr, arr + N);
    combination(0);
}