#include<iostream>
#include<cstring>

using namespace std;

int main(){
    int N;

    cin>> N;
    cin.ignore();
    string plan;
    char arr[500001] ={0, };
    int size = 0;
    int Blue = 0;
    int Red = 0;
    
    getline(cin, plan);
    int index = 0;

    for(int i = 0; i < N; i++){

        int tmp = plan[i];

        if(i == 0){
            arr[index] = tmp;
            index++;
            size++;
        }else if(i != 0 && arr[index-1] != tmp){
            arr[index] = tmp;
            index++;
            size++;
        }
    }

    for(int i = 0; i < size; i++){
        if(arr[i] == 'B'){
            Blue++;
        }else if(arr[i] == 'R'){
            Red++;
        }
    }

    
    if(Blue >= Red){
        cout<<Red+1;
        return 0;
    }else{
        cout<<Blue+1;
        return 0;
    }
    return 0;
}