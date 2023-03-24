#include<iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
	cin.tie(NULL);
    int TC;
    int N;
    
    cin>>TC;
    for(int i = 0; i < TC; i++){
        cin>>N;
        int min = 1000001;
        int max = -1000001;
        for(int i = 0; i < N; i++){
            int temp;
            cin>>temp;

            if(min > temp){
                min = temp;
            }
            if(max < temp){
                max = temp;
            }
        }
        cout<<min<<" "<<max<<'\n';
    }
    return 0;
}