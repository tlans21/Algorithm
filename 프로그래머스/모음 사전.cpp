#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<string> v;

string directory[5]= {"A", "E", "I", "O", "U"};
void dfs(string answers, int cnt){
    
    if(cnt == 5){
        return;
    }
    
    for(int i = 0; i < 5; i++){
        string next = answers + directory[i];   
        v.push_back(next);
        dfs(next, cnt + 1);
    };
}

int solution(string word) {
    int answer = 0;
    
    dfs("", 0);
    sort(v.begin(), v.end());
    answer = lower_bound(v.begin(), v.end(), word) - v.begin() + 1;
    return answer;
}