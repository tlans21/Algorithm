#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;
int N;
int sum = 0;
vector<int> arr(N);
vector<int> two(2);

int main(){
    cin>>N;
    int end = N-1;
    int start = 0;
    int min = 2000000000;
    for(int i = 0; i < N; i++){
        int num;
        cin>>num;
        arr.push_back(num);
    }
    sort(arr.begin(), arr.end());

    while(start<end){
        int sum = arr[start] + arr[end];

        if(min > abs(sum)){
            min = abs(sum);
            two[0] = arr[start];
            two[1] = arr[end];
        }

        if(sum > 0){
            end--;
        }else if(sum < 0){
            start++;
        }

        if(sum == 0){
            break;
        }
    }
    cout<<two[0]<<" "<<two[1];

    return 0;
}