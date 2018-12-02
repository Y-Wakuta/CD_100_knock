//参考にしたサイト: http://torus711.hatenablog.com/entry/20140512/1399913265
#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <iomanip>
//#include <bits/stdc++.h>

#define REP(i,n) for(ll i = 0; i < (ll)(n); i++)
#define ALL(x) (x).begin(),(x).end()

using namespace std;
using ll = long long;

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);

    //write here
    int N = 0;
    vector<int> coins;
    cin >> N;
    REP(i,N){
        ll c = 0;
        cin >> c;
        coins.push_back(c);
    }

    double p = 0;
    REP(tar,N){
        int is_yakusu = 0;
        REP(res,N)
            if(coins[tar] % coins[res] == 0)
                is_yakusu++;

        double each_p = 1.0 / is_yakusu;
        p += each_p * ((is_yakusu + 1) / 2);
    }

    cout << setprecision( 8 ) << fixed << p << endl;

    return 0;
}

/*結局正解できなかったコード
//最後に表を向いている条件は自分の左に偶数個の自分の約数が必要
int omotes = 0;
int patterns = 0;
do{
for(auto b = 0;b < N; b++) bins[b] = true;
patterns++;
int pos = 0;
while(pos < N -1){
int target = pos + 1;
while(target < N){
if(coins[target] % coins[pos] == 0)
bins[target] = !bins[target];
target++;
}
pos++;
}

omotes += accumulate(ALL(bins),0);
}while(next_permutation(ALL(coins)));
cout << (long double)omotes / (long double)patterns << endl;
*/
