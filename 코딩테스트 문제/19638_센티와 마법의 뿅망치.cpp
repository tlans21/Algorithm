#include<iostream>
#include<vector>
#include<queue>


using namespace std;
priority_queue<int, vector<int>, less<int>> q1;

int main(){
    int N;
    int H;
    int T;
    int cnt = 0;
    int maxidx = 0;
    int maxi = 0;
    bool flag = false;
    int cnt2 = 0;
    cin>>N>>H>>T;

    for(int i = 0; i < N; i++){
        int giant;
        cin>>giant;
        q1.push(giant);
    }

    //제한 횟수만큼 반복시켜 뿅망치를 사용한다.
    // 거인의 키가 전부다 1일땐 결과 값 출력
    // 센티보다 거인의 키가 전부다 작으면 출력
    // 제한 횟수만큼 반복시켜도 센티보다 거인이 크거나 같은 경우도 출력
    for(int i = 0; i < T; i++){
        if(H <= q1.top()){
            if(q1.top() == 1){
                cout<<"NO"<<'\n';
                cout<<q1.top()<<'\n';
                return 0;
            }
            int maxHeight = q1.top() / 2;
            q1.pop(); // 최댓값 변경을 위한 pop logN
            q1.push(maxHeight); // logN
            cnt++; // 뿅망치 횟수
        }
    }

    //뿅망치 횟수 전부다 소진한 이후 그래도 거인의 키가 센티보다 큰게 남아있다
    if(H <= q1.top()){
        cout<<"NO"<<'\n';
        cout<<q1.top()<<'\n';
    }else{ // 거인들의 키가 센티보다 전부다 작다
        cout<<"YES"<<'\n';
        cout<<cnt<<'\n';
    }
    //총 시간 복잡도 NlogN + T*(logN+logN) = 50만 +  10만 *(5*5) = 300만 
    return 0;
}