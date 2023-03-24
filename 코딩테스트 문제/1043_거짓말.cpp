#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
vector<vector<int>> vec(50);
vector<int> arr;


int parent[51];

int N;
int M;
int K;
int Find(int x){
    if(parent[x] == x){
        return x;
    }
    return x = Find(parent[x]);
}

void Union(int x, int y){
    x = Find(x);
    y = Find(y);

    parent[x] = y;
}
int main(){
    cin>>N>>M>>K;

    for(int i = 1; i <= N; i++){
        parent[i] = i;
    }
    int x;

    while(K--){
        cin>>x;
        arr.push_back(x);
    }
    int s;
    int num;
    int temp;
    for(int i = 0; i < M; i++){
        cin>>s;
        for(int j = 0; j < s; j++){

            if(j >= 1){
                temp = num;
                cin>>num;
                Union(temp, num);
            }else{
                cin>>num;
            }
            vec[i].push_back(num);
        }
    }

    int remain = M;

    for(auto &people : vec){
        bool flag = false;
        for(auto &person : people){
            if(flag){
                break;
            }
            for(auto &arrKnow : arr){
                if(Find(person)==Find(arrKnow)){
                    flag = true;
                    break;
                }
            }
        }
        if(flag){
            remain--;
        }
    }
    cout<<remain<<'\n';
    return 0;
}