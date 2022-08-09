#include<iostream>

int C;

long pow(long A, long B){
    if(B == 1){
        return A % C;
    }

    long temp = pow(A, B/2); 

    //짝수인 경우

    if(B % 2 == 0){
        return (temp * temp) % C;
    }
    
    //홀수인 경우

    if(B % 2 == 1){
        return (temp * temp) % C * A % C;
    }
}

using namespace std;
int main(){

    long A;
    long B;

    cin >> A >> B >> C;

    

    cout<<pow(A, B);



    return 0;
}