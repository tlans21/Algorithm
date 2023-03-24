#include<iostream>
#include<stack>
#include<vector>
#include<string>
#include<cstring>
#include<algorithm>
#include<set>

using namespace std;

string str;
bool selected[11];
int index_check[201];
stack<int> s;
set<string> same_check;
vector<pair<int, int>> indexstorge;
vector<string> solution;


void DFS(int idx, int cnt){

    if(cnt>= 1){
        string a = "";
        for(int i = 0; i < str.size(); i++){
            if(index_check[i]){
                continue;
            } // 저장된 '(',  ')'을 제외하고 출력하기위해 if문을 사용
            a = a + str[i];
        }

        if(same_check.find(a) == same_check.end()){
            same_check.insert(a);
            solution.push_back(a);
        }

    }

   for(int i = idx; i < indexstorge.size(); i++){
       if(selected[i] == true){
           continue;
       }
       selected[i] = true;
       index_check[indexstorge[i].first] = true;  // 괄호 '('의 인덱스
       index_check[indexstorge[i].second] = true; // 괄호 ')'의 인덱스
       DFS(i, cnt + 1);
       selected[i] = false;
       index_check[indexstorge[i].first] = false;
       index_check[indexstorge[i].second] = false;
   } 
}


int main(){

    cin >> str;

    for(int i = 0; i < str.size(); i++){
        if(str[i] == '('){
            s.push(i); // ( 괄호의 인덱스를 저장
        }else if(str[i] == ')'){
            indexstorge.push_back({s.top(), i}); // 괄호 쌍의 인덱스를 저장.
            s.pop(); 
        }
    }
    DFS(0, 0);

    sort(solution.begin(), solution.end());


    for(int i = 0; i < solution.size(); i++){
        cout << solution[i] <<'\n';
    }

    return 0;
}
