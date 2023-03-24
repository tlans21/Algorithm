#include<iostream>
using namespace std;

#include<iostream>

using namespace std;

int n;

void helloprinter(int arr[], int n){
    printf("hello\n");
    if(n == 0){
        return;
    }
    helloprinter(arr, n/2);
    helloprinter(arr, n/2);
};

int main(){
    int N;
    cin>>N;
    int arr[5];
    for(int i = 1; i<= N; i++){
        cin>>arr[i];
    }
    helloprinter(arr, N);
}