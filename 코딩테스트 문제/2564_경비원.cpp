#include<iostream>

using namespace std;

int main(){
    int SquareX;
    int SquareY;
    cin>>SquareX>>SquareY;
    
    int map[SquareY+1][SquareX+1]={0};
    int resturant;
    
    cin>>resturant;

    for(int i = 0; i < resturant; i++){
        int direct;
        int loc;
        
        cin>>loc>>direct;
        if(loc == 1){
            map[0][direct] = loc;
        }else if(loc == 2){
            map[SquareY][direct] = loc;
        }else if(loc == 3){
            map[direct][0] = loc;
        }else if(loc == 4){
            map[direct][SquareX] = loc;
        }
    }
    int myDirect;
    int myLoc;
    cin>>myLoc>>myDirect;
    int DistanceSum = 0;
    int Circle = 0;
    int RCircle = 0;

    //시계 방향으로 도는 경우와 반시계로 비교해야함.
    //자신의 위치를 일단 알아야함.
    for(int i = 0; i <= SquareY; i++){
        for(int j = 0; j <= SquareX; j++){
            if(map[i][j] == 1){
                if(myLoc == 1){
                    if(myDirect > j){
                        DistanceSum += (myDirect - j);
                    }else{
                        DistanceSum += (j - myDirect);
                    }
                }else if(myLoc == 2){
                   Circle = myDirect + SquareY + j;
                   RCircle = ((SquareX-myDirect) + SquareY + (SquareX-j));
                   DistanceSum +=min(Circle, RCircle);
                   Circle = 0;
                   RCircle = 0; 
                }else if(myLoc == 3){
                    //주의사항
                    Circle = myDirect + j;
                    RCircle = SquareY-myDirect+SquareX+SquareY+SquareX-j;
                    DistanceSum += min(Circle,RCircle);
                    Circle = 0;
                    RCircle = 0;
                }else if(myLoc == 4){
                    Circle = SquareY-myDirect+SquareX+SquareY+j;
                    RCircle = myDirect + SquareX-j;
                    DistanceSum += min(Circle,RCircle);
                    Circle = 0;
                    RCircle = 0;
                }
            }else if(map[i][j] == 2){
                if(myLoc == 1){
                    Circle = ((SquareX-myDirect)+SquareY+(SquareX-j));
                    RCircle = (myDirect+SquareY+j);
                    DistanceSum +=min(Circle, RCircle);
                    Circle = 0;
                    RCircle = 0;
                }else if(myLoc == 2){
                    if(j>myDirect){
                        DistanceSum += (j-myDirect);
                    }else{
                        DistanceSum += (myDirect-j);
                    }
                }else if(myLoc == 3){
                    Circle = (myDirect + SquareX + SquareY + (SquareX-j));
                    RCircle = (SquareY-myDirect + j);
                    DistanceSum += min(Circle, RCircle);
                    Circle = 0;
                    RCircle = 0;
                }else if(myLoc == 4){
                    Circle = (SquareY-myDirect+SquareX-j);
                    RCircle = ((myDirect+SquareX)+(SquareY)+j);
                    DistanceSum += min(Circle, RCircle);
                    Circle = 0;
                    RCircle = 0;
                }
            }else if(map[i][j] == 3){
                if(myLoc == 1){
                    Circle = (SquareX-myDirect+SquareY+SquareX+SquareY-i);
                    RCircle = myDirect + i;
                    DistanceSum += min(Circle, RCircle);
                    Circle = 0;
                    RCircle = 0;
                }else if(myLoc == 2){
                    Circle = (myDirect + (SquareY-i));
                    RCircle = (i+SquareX+SquareY+(SquareX-myDirect));
                    DistanceSum += min(Circle, RCircle);
                    Circle = 0;
                    RCircle = 0;
                }else if(myLoc == 3){
                    if(myDirect >  i){
                        //내가 더 아래에 있는 경우
                        DistanceSum += myDirect-i;
                    }else{
                        DistanceSum += i-myDirect;
                    }
                }else if(myLoc == 4){
                    Circle = (SquareY-myDirect)+(SquareX)+(SquareY-i);
                    RCircle = myDirect+SquareX+i;
                    DistanceSum += min(Circle, RCircle);
                    Circle = 0;
                    RCircle = 0;
                }
            }else if(map[i][j] == 4){
                if(myLoc == 1){
                    Circle = ((SquareX-myDirect)+i);
                    RCircle = myDirect+SquareY+SquareX+(SquareY-i);
                    DistanceSum+=min(Circle, RCircle);
                    Circle = 0;
                    RCircle = 0;
                }else if(myLoc == 2){
                    Circle = myDirect+SquareY+SquareX+i;
                    RCircle = (SquareY-i)+SquareX-myDirect;
                    DistanceSum +=min(Circle,RCircle);
                    Circle = 0;
                    RCircle = 0;
                }else if(myLoc == 3){
                    Circle = myDirect + SquareX + i;
                    RCircle = ((SquareY-myDirect) + SquareX + (SquareY-i));
                    DistanceSum += min(Circle, RCircle);
                    Circle = 0;
                    RCircle = 0;
                }else if(myLoc == 4){
                    if(myDirect > i){
                        DistanceSum += (myDirect - i);
                    }else{
                        DistanceSum += (i-myDirect);
                    }
                }
            }
        }
    }
    cout<<DistanceSum;
}