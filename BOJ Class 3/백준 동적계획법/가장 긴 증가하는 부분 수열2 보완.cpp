#include<iostream>

using namespace std;

int N;
int A[1000001];
int ret;
int Lis[10000001];

// 해당 문제는 dp로 풀수 없다. 왜냐하면 n의 값이 100만까지 주어져 있어 시간초과가 날 수 있기 때문이다.

int binary_search(int start, int end, int num){
    int ret;
    while(start <= end){
        int mid = (start + end) / 2;
        if(Lis[mid] >= num){
            ret = mid;
            end = mid -1;
        }else{
            start = mid + 1;
        }
    }
    return ret;
}

int main(){
    cin >> N;
    int length = 1;
    for(int i = 0; i < N; i++){
        cin>>A[i];
    }
    Lis[0] = A[0];

    for(int i = 1; i < N; i++){
        if(Lis[length - 1] < A[i]){
            Lis[length] = A[i];
            length++;
        }else{
            int idx = binary_search(0, length-1, A[i]);
            Lis[idx] = A[i];
        }
    }
    cout<<length;
    return 0;
}