#include <string>
#include <vector>
#include<algorithm>
#include<iostream>

using namespace std;

int compare(string a, string b){
    return a+b > b+a;
}
string solution(vector<int> numbers) {
    string answer = "";
    vector<string> temp;
    //가장 큰 수를 만들기 위해서는 제일 처음 앞자리가 가장 커야합니다.
    //그러므로 앞자리가 가장 큰 값을 기준으로 정렬을 해야합니다.
    //수가 같으면 자리가 차지하는 수가 작은 경우로.

    for(int i = 0; i < numbers.size(); i++){
        temp.push_back(to_string(numbers[i]));
    }
    sort(temp.begin(), temp.end(), compare);
    if(temp[0] == "0"){
        return "0";
    }
    for(int i = 0; i < temp.size(); i++){
        answer+=temp[i];
    }
    return answer;
}