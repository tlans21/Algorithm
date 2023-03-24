#include <string>
#include <vector>
#include <queue>
using namespace std;

string solution(vector<string> cards1, vector<string> cards2, vector<string> goal) {
    string answer = "";
    queue<string> q;
    
    for(int i = 0; i < goal.size(); i++){
        q.push(goal[i]);
    }
    int i = 0;
    int j = 0;
    bool flag = true;
    while(!q.empty()){
        if(q.front() == cards1[i]){
            q.pop();
            i++;
        }else if(q.front() == cards2[j]){
            q.pop();
            j++;
        }else if(q.front() != cards1[i] && q.front() != cards2[j]){
            flag = false;
            break;
        }
    }
    
    if(flag == true){
        answer = "Yes";
    }else if(flag == false){
        answer = "No";
    }
    
    return answer;
}