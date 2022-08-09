#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main(){
    vector<int> vec[51];
    int dp[51][1001] = {0,};
    int N;
    int M;
    int h;
    cin>>N>>M>>h;

    cin.ignore(1);

    for(int i = 1; i <= N; i++){
        string temp;
        getline(cin, temp, '\n');

        for(int j = 0; j <temp.size(); j++){
            if(temp[j] == ''|| j == 0){
                vec[i].push_back(stoi(&temp[j]));
            }
        }
    }
}