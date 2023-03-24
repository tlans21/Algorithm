#include<iostream>

using namespace std;

int main(){
    int N;
    cin>>N;

    int answer = 1;

    for(int i = 1; i <= 100; i++){
        answer = i * N;
        cout<<answer<<'\n';    
    }


}


