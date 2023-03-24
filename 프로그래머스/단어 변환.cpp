#include <string>
#include <vector>

using namespace std;
int visit[51];
int temp = 987654321;
bool diff(string a, string b){
    int cnt = 0;
    for(int i = 0; i < a.size(); i++){
        if(a[i] != b[i]){
            cnt++;
        }
    }
    if(cnt == 1){
        return true;
    }else{
        return false;
    }
}

int dfs(vector<string> words, string begin, string target, int depth){
    if(temp <= depth){
        return 0;
    }
    
    if(begin == target){
        temp = min(temp, depth);
        return temp;
    }

    for(int i = 0; i < words.size(); i++){
        if(visit[i] == 1){
            continue;
        }
        if((diff(begin, words[i]) == true) && !visit[i]){
            visit[i] = 1;
            dfs(words, words[i], target, depth + 1);
            visit[i] = 0;
        }else{
            continue;
        }
    }
    return 0;
}


int solution(string begin, string target, vector<string> words) {
    dfs(words, begin, target, 0);
    if(temp == 987654321){
        return 0;
    }
    return temp;
}