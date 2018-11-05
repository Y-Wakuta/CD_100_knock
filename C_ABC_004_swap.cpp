#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
//#include <bits/stdc++.h>

#define REP(i,n) for(ll i = 0; i < (ll)(n); i++)
#define ALL(x) (x).begin(),(x).end()

using namespace std;
using ll = long long;

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);

    //write here
    int cards[] = {1,2,3,4,5,6};
    ll N = 0;
    ll n= 0;
    cin >> N;
    REP(i,N){
        //一定回数同じ回数swapして初期値に戻ってくるならそれでNを剰余する
        if(cards[0] == 1 && cards[1] == 2 && cards[2] ==3 && cards[3] == 4 && cards[4] == 5 && cards[5] == 6 && n == 0 && i > 0) {
            n = i;
            i = n * (N / n);
            if(i == N)//Nがちょうどnで割り切れる時(この場合30)の時はそれ以上swapしないようにする
                break;
        }
        int left=  i % 5;
        int right = i % 5 + 1;
        swap(cards[left],cards[right]);
    }

    REP(i,6)
        cout << cards[i];

    cout << endl;
    return 0;
}
