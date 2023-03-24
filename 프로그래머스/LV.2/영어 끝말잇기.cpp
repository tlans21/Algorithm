#include <string>
#include <vector>
#include <iostream>
#include <map>
using namespace std;

map<string, int> m;
vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    int cycle = 0;
    int turn = 0;
    bool CheckBreak = true;
    string temp = "";
    //탈락 기준 : 같은 것을 말한 경우, 그리고 끝 글자와 첫글자가 다른 경우
    for(int i = 0; i < words.size(); i++){
        turn = (i % n) + 1;
        cycle = (i / n) + 1;
        if(!temp.empty() && temp.back() != words[i][0]){
            answer.push_back(turn);
            answer.push_back(cycle);
            CheckBreak = false;
            break;
        }
        if(m.find(words[i]) != m.end()){
            answer.push_back(turn);
            answer.push_back(cycle);
            CheckBreak = false;
            break;
        }else if(m.find(words[i]) == m.end()){
            m[words[i]]++;
        }
        temp+=words[i];
    }
    if(CheckBreak == true){
        answer.push_back(0);
        answer.push_back(0);
    }
    
    return answer;
}