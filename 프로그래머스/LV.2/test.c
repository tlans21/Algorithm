#include <stdio.h>

int main(){
    int score;
    scanf("%d", score);
    switch(score){
        case 90: 
            printf("A");
        case 80:
            printf("B");
        case 70:
            printf("C");
        case 60:
            printf("D");
        case 50:
            printf("E");
    }
}
sub(int x, int y){
    x = x + 1;
    y = y + 1;
}

int main(void){
    int data[5] = {1, 2, 3, 4, 5};
    int a = 1;

    sub(a, data[a]);
    sub(a, data[a]);
}