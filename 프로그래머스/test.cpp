#include<iostream>
#include<vector>

using namespace std;

int main(){
    vector<vector<string>> v;
    vector<string> v1;
    string str;
    int N;
    cin>>N;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < 2; j++){
            cin>>str;
            v[i].push_back(str);
        }
    }
}