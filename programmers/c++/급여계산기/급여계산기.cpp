// 열혈 cpp 문제
# include <iostream>

using namespace std;

int main(){
    int basic_pay=50, sold_price;
    while(1)
    {
        cout << "판매금액 :";
        cin >> sold_price;

        if (sold_price == -1)
            break;

        cout << "월급 :" << 50 + sold_price*0.12 << "만원" << endl;
    }
    return 0;
}