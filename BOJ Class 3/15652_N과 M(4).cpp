#include<iostream>
#include<vector>

using namespace std;

bool visited[9];
vector<int> a;
int arr[9];
int N;
int M;

void combination(int idx, int cnt){
    if(M == cnt){
        for(int i = 0; i < M; i++){
            cout<<a[i]<<' ';
        }
        cout<<endl;
        return;
    }
    for(int i = idx; i < N; i++){
        visited[i] = true;
        a.push_back(arr[i]);
        combination(i, cnt + 1);
        visited[i] = false;
        a.pop_back();
    }
}

int main(){


    cin>> N >> M;
    for(int i = 0 ; i < N; i++){
        arr[i]= i+1;
    }
    combination(0, 0);
}