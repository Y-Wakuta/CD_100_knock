#include <iostream>
#include <vector>
#include <string>
#include <bits/stdc++.h>
 
#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define ALL(x) (x).begin(),(x).end()
 
using namespace std;
using ll = long long;
using tp = tuple<ll,ll,ll,ll>;
 
// タプルの最初の要素から順番に比較　もしその要素が同じなら次の要素で比較
bool mycompare( const tp &lhs, const tp &rhs )
{
    return std::get<2>(lhs) < std::get<2>(rhs);
}
 
 
int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
 
    //write here
    ll N,M;
    vector<tp> pv;
 
    cin >> N >> M;
    REP(i,M){
        ll p,y;
        cin >> p >> y;
        pv.push_back(make_tuple(p,y,i,0));
    }
 
    sort(ALL(pv));
 
    int p = 0;
    int counter =0;
    REP(i,M){
        counter++;
        if( p == std::get<0>(pv[i])){
            std::get<3>(pv[i]) = counter;
        }
        else{
            counter = 1;
            std::get<3>(pv[i]) = counter;
            p = get<0>(pv[i]);
        }
    }
 
    sort(pv.begin(),pv.end(),mycompare);
 
    REP(i,M){
        std::ostringstream su;
        su << std::setw(6) << std::setfill('0') << get<0>(pv[i]);
        std::ostringstream sl;
        sl << std::setw(6) << std::setfill('0') << get<3>(pv[i]);
 
        string s(su.str() + sl.str());
        cout << s << endl;
    }
 
    return 0;
}      
