#include<iostream>
#include<stack>
using namespace std;

int main(){
    int N;
    cin>>N;

    int arr[100001];
    char temp[200003];
    stack<int> s;
    for(int i = 0; i < N; i++){
        cin>>arr[i];
    }
    int idx = 0;
    int num = 1;
    int count = 0;
    while(1){
        if(num <= arr[idx]){
            s.push(num++);
            temp[count++] = '+';
        }else if(s.top() == arr[idx]){
            s.pop();     
            idx++;
            temp[count++] = '-';
        }else{
            cout<<"NO"<<'\n';
            return 0;
        }



        if(idx == N){
            break;
        }
    }
    for(int i = 0; i <= count-1; i++){
        cout<<temp[i]<<'\n';
    }
    return 0;
}