#include<iostream>

using namespace std;

int loc1; // 첫 번째 자리 수
int loc2; // 두 번째 자리 수
int loc3; // 세 번째 자리 수
int loc4; // 네 번째 자리 수

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int P;
    int M;
    int T;
    int sum;
    int cnt;
    int check[10001] ={0};
    cin>>P;
    for(int i = 1; i <= P; i++){
        cin>>T>>M; // 값 입력 받기
        cnt = 0;
        sum = M; // 초기 합
        int loop = 0;
        //소수인지 검사
        
        for(int j = 1; j <= M; j++){
            if(sum % j == 0){
                //만약이 1부터 M까지 나눠어지는지 확인
                //cnt가 2개 즉, 1과 M 즉 입력한 값만은 무조건 나눠지므로 cnt가 2인경우 소수
                cnt++;
            }
        }
        if(cnt != 2){
            cout<<i<<" "<<M<<" "<<"NO"<<'\n';
            continue;
        }
        while(1){
            //연산을 반복했을 때 1인 경우
            check[sum] = 1;
            loop++;
            if(sum == 1){
                cout<<i<<" "<<M<<" "<<"YES"<<'\n';
                break;
            }else{
                // 각 자리
                //ex) 313
                loc1 = sum % 10; // 3
                loc2 = (sum % 100); // 13
                loc3 = sum % 1000; // 313
                loc4 = sum % 10000; // 0313

                int temp1 = loc1;
                int temp2 = loc2 / 10;
                int temp3 = loc3 / 100;
                int temp4 = loc4 / 1000; 
                //각 자리 수를 구하고 제곱하고 합하는 과정
                temp1 *=temp1;
                temp2 *=temp2;
                temp3 *=temp3;
                temp4 *=temp4;

                sum = (temp1 + temp2 + temp3 + temp4);
                if(check[sum] == 1){
                    //사이클이 생긴 경우
                    if(sum == 1){
                        //그 중에서 1이 나와 행복한 소수가 됨
                        cout<<i<<" "<<M<<" "<<"YES"<<'\n';
                    }else{
                        cout<<i<<" "<<M<<" "<<"NO"<<'\n';
                    }
                }else{
                    //사이클이 생기지 않은 경우

                }
            }
        }
    }
}