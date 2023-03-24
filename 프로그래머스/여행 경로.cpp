#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool visit[10001] = {0};

vector<string> res;
bool dfs(vector<vector<string>> tickets, string start, int depth){
    res.push_back(start);
    if(tickets.size() == depth){
        return true;
    }
    for(int i = 0; i < tickets.size(); i++){
        if(tickets[i][0] == start && visit[i] == 0){
            visit[i] = 1;
            string next = tickets[i][1];
            int s = dfs(tickets, next, depth+1);
            if(s){
                return true;
            }
            visit[i] = 0;
        }
    }
    res.pop_back();
    return false;
}
vector<string> solution(vector<vector<string>> tickets) {
    vector<string> answer;
    sort(tickets.begin(), tickets.end()); // 알파벳순 정렬을 위함이다.
    dfs(tickets, "ICN", 0);
    answer = res;
    return answer;
}