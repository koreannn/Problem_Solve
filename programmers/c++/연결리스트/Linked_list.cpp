#include <iostream>

using namespace std;

class Node {
    public:
        int data;
        Node* next;

        Node(int val) : data(val), next(nullptr){}
};

class LinkedList {
    private:
        Node* head;
    public:
        LinkedList() : head(nullptr) {}

        // 맨 뒤에 노드 추가
        void append(int val){
            Node* newNode = new Node(val);
            if(!head){ //head가 비어있을 때
                head = newNode;
                return;
            }
            Node* current = head;
            while(current -> next){
                current = current -> next;
            }
            current -> next = newNode;
        }

        // 맨 앞에 노드 추가
        void push(int val){
            Node* newNode = new Node(val);
            newNode -> next = head;
            head = newNode;
        }

        // (특정한 값을 가진) 노드 삭제
        void remove(int val){
            if (!head) return; // head가 비어있으면 return
            
            if(head -> data == val){
                Node* temp = head;
                head = head -> next;
                delete temp;
                return;
            }

            Node* current = head;
            while (current -> next && current -> next -> data != val){
                current = current -> next;
            }

            if (current -> next){
                Node* temp = current -> next;
                current -> next = current -> next -> next;
                delete temp;
            }
        }

        // 리스트 출력
        void disp(){
            Node* current = head;
            while (current){
                Node* temp = current;
                cout << current -> data << " -> ";
                current = current -> next;
            }
            cout << "nullptr" << std::endl;
        }

        // 소멸자(메모리 해제)
        ~LinkedList(){
            Node* current = head;
            while (current){
                Node* temp = current;
                current = current -> next;
                delete temp;
            }
        }
};

int main(){
    LinkedList list;

    list.append(1);
    list.append(2);
    list.append(3);
    list.push(5);

    cout << "초기 리스트 : ";
    list.disp();

    list.remove(2);
    cout << "2 삭제 후 : ";
    list.disp();

    list.push(0);
    cout << "0 추가 후 : ";
    list.disp();

    return 0;
}