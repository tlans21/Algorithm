#include<iostream>

using namespace std;

bool check = false;


int main(){
    int arr[28];
    for(int i = 0; i < 28; i++){
        cin>>arr[i];
    }

    for(int i = 1; i <= 30; i++){
        for(int j = 0; j < 28; j++){
            if(arr[j] == i){
                check = true; // 존재한다.
            }
        }

        if(!check){
            cout<<i<<'\n';
        }
        check = false;
    }
    return 0;
}