#include<iostream>

using namespace std;

typedef struct Node{
    int data;
    Node *next;
}Node;

typedef struct queue{
    Node *front;
    Node *rear;
    int count; 
}queue;


int size(queue *q){
    return q->count;
}

int empty(queue *q){
    if(q->count == 0){
        return 1;
    }else{
        return 0;
    }
}
void initQueue(queue *q){
    q->front = q->rear = NULL; // queue라는 구조체 포인터가 구조체 포인터 front를 가리킵니다.
    q->count = 0;
}
void push(queue *q, int num){
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = num; //data의 값을 참조
    newNode->next = NULL; //next 포인터가 가리키는 주소는 아무것도 가리키지않는다.

    if(empty(q)){
        q->front = newNode; // 비어있을 때, front는 새로 생성한 노드를 가리킨다.
    }else{
        q->rear->next = newNode;  // 비어있지 않을 때 현재 rear의 next포인터가 가리키는, 즉 전에 생성되었던 노드의 next포인터에 새로운 생성한 노드를 가리킨다. 
    }
    q->rear = newNode; // rear포인터를 새롭게 생성한 노드를 가리키도록 갱신
    q->count++;
}

int pop(queue *q){
    if(empty(q)){
        return -1;
    }else{
        int value;
        Node *DeleteNode; // 삭제할 노드를 가리키는 포인터를 만듬
        DeleteNode = q->front; // front가 가리키는 노드를 DeleteNode가 가리키도록 함
        value = DeleteNode->data; // 삭제될 노드의 data값을 value에 저장
        q->front = DeleteNode->next; // front가 다음 노드를 가리키도록 함.
        q->count--;
        return value;
    }
}

int front(queue *q){
    if(empty(q)){
        return -1;
    }else{
        return q->front->data;
    }
}

int back(queue *q){
    if(empty(q)){
        return -1;
    }else{
        return q->rear->data;
    }
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int N;
    cin>>N;
    queue q;
    initQueue(&q);

    for(int i = 0; i < N; i++){
        
        string str;
        
        cin>>str;

        if(str == "push"){
            int num;
            cin>>num;
            push(&q, num);
        }else if(str == "pop"){
            cout<<pop(&q)<<'\n';
        }else if(str == "size"){
            cout<<size(&q)<<'\n';
        }else if(str == "empty"){
            cout<<empty(&q)<<'\n';
        }else if(str == "front"){
            cout<<front(&q)<<'\n';
        }else if(str == "back"){
            cout<<back(&q)<<'\n';
        }
    }   
}