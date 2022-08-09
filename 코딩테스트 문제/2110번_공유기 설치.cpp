#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

vector<int> wifi;

int find(int n, int c){

    int left_dist = 0;
    int right_dist = wifi[n-1]-1;

    int result_dist;

    while(left_dist<=right_dist){
        int install = 1;

        int mid_dist = (left_dist+right_dist)/2;

        int start = wifi[0];

        for(int i = 1; i <n; ++i){
            int end = wifi[i];

            if(end - start >= mid_dist){
                install +=1;
                start =end;
            }
        }
        if(install >= c){
            result_dist = mid_dist;

            left_dist = mid_dist + 1;
        }else{
            right_dist = mid_dist - 1;
        }
    }

    return result_dist;
}


int main(){
    int n;
    int c;
    cin>>n>>c;

    int location;

    for(int i = 0; i <n; ++i){
        cin>>location;
        wifi.push_back(location);
    }
    sort(wifi.begin(), wifi.end());
    cout<< find(n, c);

    return 0;
}