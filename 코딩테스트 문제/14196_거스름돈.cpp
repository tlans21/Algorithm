#include<iostream>

using namespace std;

int main(){
    int N;

    cin>>N;
    int five = 0;
    int three = 0 ;
    int remain;
    int count = 0;
    five = N / 5;
    remain = N % 5;

    if(remain == 0){
        count = five;
        cout<<count;
        return 0;
    }//처음 5의 배수로 나뉘어떨어지는지 검사

    while(1){
        //2로 나뉘어 떨어지는 경우
        if(remain % 2 == 0){
            three = remain / 2;
            count += three;
            count += five;
            break;
        }else{
            //안 나뉘어질 경우 5를 하나 뺀다.
            five = five - 1;
            remain = remain + 5;
        }
        if(five == -1){
            cout<<-1;
            return 0;
        }
    }
    cout<<count;
    return 0;
}