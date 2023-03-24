#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int solution(int k, vector<int> tangerine) {
    int answer = 0;
    map<int, int> m;
    
    for(int i = 0; i < tangerine.size(); i++){
        if(m.find(tangerine[i]) == m.end()){
            m.insert({tangerine[i], 1});
        }else{
            m[tangerine[i]]++;
        }
    }
    vector<int> v;
    for(auto a : m){
        v.push_back(a.second);
    }
    int cnt = 0;
    sort(v.begin(), v.end(), greater<int>());
    
    for(int i = 0; i < v.size(); i++){
        answer++;
        cnt += v[i];
        if(k <= cnt){
            break;
        }
    }
    
    return answer;
}