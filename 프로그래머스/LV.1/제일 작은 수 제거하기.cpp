#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    int temp = 123456789;
    int idx = 0;
    
    for(int i = 0; i < arr.size(); i++){
        if(temp >= arr[i]){
            temp = arr[i];
            idx = i;
        }
    }
    arr.erase(arr.begin() + idx);
    if(arr.size() == 0){
        answer.push_back(-1);
    }else{
        for(int i = 0; i < arr.size(); i++){
            answer.push_back(arr[i]);
        }
    }
    return answer;
}