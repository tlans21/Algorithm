#include<iostream>
#include<vector>

using namespace std;
using matrix = vector<vector<long long>>;
matrix temp;

long long N;
matrix Do(matrix &A, matrix &B){
    matrix temp(2, vector<long long>(2)); // 초기화
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 2; j++){
            for(int k = 0; k < 2; k++){
                temp[i][j] += A[i][k] * B[k][j];
            }
            temp[i][j] = temp[i][j] % 1000000007;
        }
    }
    return temp;
}

int main(){
    cin>>N;
    matrix A = {{1, 1},{1, 0}};
    matrix unit = {{1, 0}, {0, 1}};

    while(N>0){
        if(N % 2 == 1){
         unit = Do(unit, A);
        }
        A = Do(A, A);
        N = N/2;
    }
    cout<<unit[0][1];
}