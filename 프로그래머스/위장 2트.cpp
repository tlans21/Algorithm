#include <string>
#include <vector>
#include <map>
using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    map<string, int> m;
    for(int i = 0; i < clothes.size(); i++){
        string a = clothes[i][0];
        string b = clothes[i][1];
        m[b]++;
    }
    map<string, int> ::iterator iter;
    for(iter = m.begin(); iter != m.end(); iter++){
        answer = answer * (iter->second + 1);
    }
    answer = answer - 1;
    return answer;
}