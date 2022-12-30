#include<iostream>

using namespace std;

int main(){
    string input;
    
    int Ccnt = 0;
    int Hcnt = 0;
    int Ocnt = 0;
    int M1_Ccnt = 0;
    int M1_Hcnt = 0;
    int M1_Ocnt = 0;
    int M2_Ccnt = 0;
    int M2_Hcnt = 0;
    int M2_Ocnt = 0;
    int PlusIndex;
    int SameIndex;
    int H3 = 0;
    int H2 = 0;
    int H1 = 0;
    int C3 = 0;
    int C2 = 0;
    int C1 = 0;
    int O3 = 0;
    int O2 = 0;
    int O1 = 0;
    string str[3];
    cin>>input;

    for(int i = 0; i < input.length(); i++){
        if(input[i] == '+'){
            PlusIndex = i;
        }
        if(input[i] == '='){
            SameIndex = i;
        }
    }
    for(int i = 0; i < PlusIndex; i++){
        str[0] = str[0] + input[i];
    }
    for(int i = PlusIndex+1; i < SameIndex; i++){
        str[1] = str[1] + input[i];
    }
    for(int i = SameIndex+1; i < input.length(); i++){
        str[2] = str[2] + input[i];
    }
    
    for(int i = 0; i < str[0].length(); i++){
        if(str[0][i] >='2' && str[0][i] <= '9'){
            if(str[0][i-1] == 'C'){
                M1_Ccnt = M1_Ccnt - 1 + (str[0][i] - '0'); 
            }else if(str[0][i-1] == 'H'){
                M1_Hcnt = M1_Hcnt - 1 + (str[0][i] - '0');
            }else if(str[0][i-1] == 'O'){
                M1_Ocnt = M1_Ocnt - 1 + (str[0][i] - '0');
            }
        }
        if(str[0][i] == 'C'){
            M1_Ccnt = M1_Ccnt + 1;
        }
        if(str[0][i] == 'H'){
            M1_Hcnt = M1_Hcnt + 1;
        }
        if(str[0][i] == 'O'){
            M1_Ocnt = M1_Ocnt + 1;
        }
    }

    for(int i = 0; i < str[1].length(); i++){
        if(str[1][i] >='2' && str[1][i] <= '9'){
            if(str[1][i-1] == 'C'){
                M2_Ccnt = M2_Ccnt - 1 + (str[1][i] - '0'); 
            }else if(str[1][i-1] == 'H'){
                M2_Hcnt = M2_Hcnt - 1 + (str[1][i] - '0');
            }else if(str[1][i-1] == 'O'){
                M2_Ocnt = M2_Ocnt - 1 + (str[1][i] - '0');
            }
        }
        if(str[1][i] == 'C'){
            M2_Ccnt = M2_Ccnt + 1;
        }
        if(str[1][i] == 'H'){
            M2_Hcnt = M2_Hcnt + 1;
        }
        if(str[1][i] == 'O'){
            M2_Ocnt = M2_Ocnt + 1;
        }
    }

    for(int i = 0; i < str[2].length(); i++){
        if(str[2][i] >='2' && str[2][i] <= '9'){
            if(str[2][i-1] == 'C'){
                Ccnt = Ccnt - 1 + (str[2][i] - '0'); 
            }else if(str[2][i-1] == 'H'){
                Hcnt = Hcnt - 1 + (str[2][i] - '0');
            }else if(str[2][i-1] == 'O'){
                Ocnt = Ocnt - 1 + (str[2][i] - '0');
            }
        }
        if(str[2][i] == 'C'){
           Ccnt = Ccnt + 1;
        }
        if(str[2][i] == 'H'){
            Hcnt = Hcnt + 1;
        }
        if(str[2][i] == 'O'){
            Ocnt = Ocnt + 1;
        }
    }
    


    for(int M_1 = 1;  M_1 <= 10; M_1++){
        for(int M_2 = 1; M_2 <= 10; M_2++){
            for(int M_3 = 1; M_3 <= 10; M_3++){
                C3 = Ccnt * M_3;
                H3 = Hcnt * M_3;
                O3 = Ocnt * M_3;
                 
                if(C3 == (M_2 * M2_Ccnt) + (M_1 * M1_Ccnt) && H3 == (M_2 * M2_Hcnt) + (M_1 * M1_Hcnt) && O3 == (M_2 * M2_Ocnt) + (M_1 * M1_Ocnt)){
                    cout<<M_1<<" "<<M_2<<" "<<M_3;
                    return 0;
                }
                C3 = 0;
                H3 = 0;
                O3 = 0;
            }
        }
    }
    
    return 0;
}