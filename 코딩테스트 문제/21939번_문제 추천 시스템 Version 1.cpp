    #include<iostream>
    #include<queue>
    #include<map>

    using namespace std;

    priority_queue<pair<int, int>> maxheap;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minheap;
    map<int, int> m;
    int main(){
        int N;
        int M;
        int L;
        int P;
        int command;
        cin>>N;
        for(int i = 0; i < N; i++){
            cin>>P>>L;
            m[P] = L;
            maxheap.push(make_pair(L, P));
            minheap.push(make_pair(L, P));
        }
        cin>>M;
        for(int i = 0; i < M; i++){
            string command;
            cin>>command;
            if(command == "recommend"){
                int x;
                cin>>x;
                if(x == 1){
                    while(maxheap.top().first != m[maxheap.top().second]){
                        maxheap.pop();  // 저장해둔 데이터와 우선순위에 저장된 데이터가 다른 경우, solved의 영향을 받은걸로 간주하고 pop()합니다.
                    }
                    cout<<maxheap.top().second<<'\n';
                }else{
                    while(minheap.top().first != m[minheap.top().second]){
                        minheap.pop();
                    }
                    cout<<minheap.top().second<<'\n';
                }
            }else if(command == "add"){
                int a; // 우선순위에 넣을려는 난이도
                int b; // 우선 순위에 넣을려는 문제 번호
                cin>>b>>a;
                maxheap.push(make_pair(a, b));
                minheap.push(make_pair(a, b));
                m[b] = a;
            }else if(command == "solved"){
                int x;
                cin >> x;
                m[x] = 0;
            }
        }   
        return 0;
    }