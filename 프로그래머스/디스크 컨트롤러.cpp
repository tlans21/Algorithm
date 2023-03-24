#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

struct cmp {
    bool operator()(vector<int> a, vector<int> b) {
        return a.at(1) > b.at(1);
    }
};

int solution(vector<vector<int>> jobs) {
    int answer = 0, idx = 0, time = 0;
    sort(jobs.begin(), jobs.end());
    priority_queue<vector<int>, vector<vector<int>>, cmp> pq;
    
    
    while(idx < jobs.size() || !pq.empty()){
        
        if(idx  < jobs.size() && time >= jobs[idx][0]){
            pq.push(jobs[idx]);
            idx++;
            continue;
        }
        
        
        if(!pq.empty()){
            time += pq.top()[1]; // 작업시간을 추가.
            answer += time - pq.top()[0]; // 작업시간 - 요청시간을 빼
            pq.pop(); 
        }else{
            // 우선순위 큐가 비게 되면 현재시간에서 처리할 수 있는 작업을 전부 수행한 것이므로
            //이동한 idx를 사용
            time = jobs[idx][0];
        }
    }
    
    return answer / jobs.size();
}