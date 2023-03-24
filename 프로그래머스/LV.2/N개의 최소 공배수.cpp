#include <string>
#include <vector>

int gcd(int a, int b){
    int c;
    while(b != 0){
        c = a % b;
        a = b;
        b = c;
    }
    return a;
}

using namespace std;

int solution(vector<int> arr) {
    int answer = 0;
    int temp = arr[0];
    if(arr.size() == 1){
        return arr[0];
    }
    for(int i = 1; i < arr.size(); i++){
        temp = (temp * arr[i]) / gcd(temp, arr[i]);
    }
    answer = temp;
    return answer;
}