#include <iostream>
#include <vector>
#include <algorithm>

int compare(int a, int b){
    return a > b; // 참이면 자리를 바꾸지 않고 거짓이면 자리를 바꾼다. 결론
}
using namespace std;

vector<int> arr;

int main(){
    for(int i = 9; i >= 0; i--){
        arr.push_back(i);
    }
    
    sort(arr.begin(), arr.end(), compare);
    for(int i = 0; i <= 9; i++){
        cout<<arr[i]<<'\n';
    }
    
    return 0;
}