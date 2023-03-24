#include<iostream>

using namespace std;

int main(){
    int A;
    int B;
    int cnt = 0;

    cin>>A>>B;
    while(1){
        if(A > B){
            cout<<"-1"<<endl;
            break;
        }
        if(A == B){
            cnt++;
            cout<<cnt<<endl;
            break;
        }
        if(B % 2 == 0){
            B = B / 2;
        }else if(B % 10 == 1){
            B--;
            B = B / 10;
            }else{
            cout<<-1<<endl;
            break;
        }
        cnt++;
    }
    return 0;
}