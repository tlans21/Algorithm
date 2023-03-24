#include <string>
#include <vector>

using namespace std;

int solution(string name) {
    int answer = 0;
    int n = name.length();
    int temp = n - 1;
    for(int i = 0; i < name.size(); i++){
        if(name[i] - 'A' < 14){
            answer += name[i] - 'A';
        }else{
            answer += 'Z' - name[i] + 1;
        }
        
        int ind = i+1;
        
        while(name[ind] == 'A' && ind < name.size()){
            ind++;
        }
        temp = min(temp, i + n - ind + min(i, n - ind));
    }
    answer +=temp;
    return answer;
}