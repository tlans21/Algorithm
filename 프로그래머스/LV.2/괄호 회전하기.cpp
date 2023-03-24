#include <string>
#include <vector>
#include <stack>
using namespace std;

int solution(string s) {
    int answer = 0;
    
    for(int i = 0; i < s.size(); i++){
        stack<char> st;
        bool flag = false;
        for(int j = 0; j < s.size(); j++){
            if(s[j] == '[' || s[j] == '(' || s[j] == '{'){
                st.push(s[j]);
                flag = false;
            }else{
                if(s[j] == ']' && st.top() == '['){
                    st.pop();
                    flag = true;
                }
                if(s[j] == ')' && st.top() == '('){
                    st.pop();
                    flag = true;
                }
                if(s[j] == '}' && st.top() == '{'){
                    st.pop();
                    flag = true;
                }
            }
        }
        if(st.empty() && flag){
            answer++;
        }
        char x = s.front();
        s.erase(s.begin());
        s.push_back(x);
    }
    
    return answer;
}