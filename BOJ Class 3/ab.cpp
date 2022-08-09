#include<iostream>
#include<vector>

using namespace std;

int main(){
    vector<int> arr;
    int N;
    
    for(int i = 0; i < N; i++){
        int temp;
        cin>>temp;
        arr.push_back(temp);
    }

    for(int i = 0; i < arr.size(); i++){
        for(int j = i + 1; j < N; j++){
            if(arr[i] < arr[j]){
                
            }
        }
    }
}