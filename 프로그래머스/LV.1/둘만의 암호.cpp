#include <string>
#include <vector>

using namespace std;

string solution(string s, string skip, int index) {
    string answer = "";
    for(auto c : s){
        int t = 0;
        int v = c - 'a';
        while(t < index){
            v++;
            c = v % 26 + 'a';
            
            if(skip.find(c) == string::npos){
                //찾을수 없다면
                t++;
            }
        }
        answer+=c;
    }
    return answer;
}