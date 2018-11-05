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
    ll T,N,M;
    vector<ll> A,B;

    cin >> T;
    cin >> N;
    REP(i,N){
        ll a;
        cin >> a;
        A.push_back(a);
    }
    cin >> M;
    REP(i,M){
        ll b;
        cin >> b;
        B.push_back(b);
    }
    
    
    ll tako_counter = 0;
    ll customer_counter = 0;
    if(N < M){//そもそもたこ焼きを売れない場合
        cout << "no" << endl;
        return 0;
    }
    while(1){
        ll diff = B[customer_counter]-A[tako_counter];
        if(0 <= diff && diff <= T){//売れるたこ焼きがある場合
            tako_counter++;
            customer_counter++;
            if(customer_counter == M){//全ての客に行き渡った場合
                cout << "yes" << endl;
                return 0;
            }}else{
            tako_counter++;
            if(tako_counter > N){//たこ焼き全てについて操作し終わったが客に行き渡っていない場合
                cout << "no" << endl;
                return 0;
            }
        }
    }
}
