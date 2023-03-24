#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int compare(int a, int b){
    return a > b; // false시 오름차순으로 정렬
}
long long solution(long long n) {
    long long answer = 0;
    vector<int> arr; 
    
    while(n){
        int k = n % 10;
        arr.push_back(k);
        n = n / 10;
    }
    sort(arr.begin(), arr.end(), compare);
    
    
    for(int i = 0; i < arr.size(); i++){
        answer = answer * 10 + arr[i];
    }
    
    return answer;
}