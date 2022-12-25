#include<iostream>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;
vector<int> arr;
vector<int> answer;


int main(){
    int N;
    cin>>N;

    for(int i = 0; i < N; i++){
        int number;
        cin>>number;
        arr.push_back(number);
    }
    sort(arr.begin(), arr.end());
    int element;
    for(int i = 0; i <= 3; i++){
        for(int j= i+1; j <=3; j++){
            string num = "";
            num += to_string(arr[i]);
            num += to_string(arr[j]);
            element = stoi(num);
            answer.push_back(element);
            num = "";
            num += to_string(arr[j]);
            num += to_string(arr[i]);
            element = stoi(num);
            answer.push_back(element);
        }
    }
    sort(answer.begin(), answer.end());
    
    cout<<answer[2]<<'\n';
}