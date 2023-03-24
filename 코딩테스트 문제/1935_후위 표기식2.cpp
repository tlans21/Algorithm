#include<iostream>
#include<stack>



using namespace std;

int alpha[26];

int main(){


    stack<double> s;
    int N;
    string str;
    cin>>N;
    cin>>str;

    for(int i = 0; i < N; i++){
        cin>>alpha[i];
    }

    for(int i = 0; i < str.length(); i++){
        if(str[i] == '+' || str[i] == '-' || str[i] == '/' || str[i] == '*'){
            double a = s.top();
            s.pop();
            double b = s.top();  // 스택에 있는 피연산자 2개를 빼오는 행위
            s.pop();
            
            switch (str[i])
            {
            case '+' : s.push(b+a);
            break;
            
            case '-' : s.push(b-a);
            break;

            case '/' : s.push(b/a);
            break;

            case '*' : s.push(b*a);
            break;
            }
        }else{
            s.push(alpha[str[i]-'A']);
        }
    }
    double solution = s.top();
    cout << fixed;
    cout.precision(2);

    cout<<solution<<endl;
return 0;
}