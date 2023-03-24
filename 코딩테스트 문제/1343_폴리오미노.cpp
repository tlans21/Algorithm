#include<iostream>
#include<cstring>

using namespace std;

int main(){
    string input;
    string answer;
    cin>>input;

    if(input.size() == 1 && input[0] == 'X'){
        cout<<-1<<endl;
        return 0;
    }

    int i = 0;
    int count = 0;
    while(input[i] != '\0'){

        while(input[i] == 'X' || input[i] != '.'){
            i++;
            count++;

            if(input[i] == '\0'){
                break;
            }
        }

        if(count % 2 == 0){
            while(count >= 4){
                answer += "AAAA";
                count -=4;
            }
            while(count>=2){
                answer += "BB";
                count-=2;
            }
        }
        if(count != 0){
            cout<<-1;
            return 0;
        }
        if(input[i] == '.'){
            answer +=".";
            i++;
        }
    }
    cout<<answer;

    return 0;


}