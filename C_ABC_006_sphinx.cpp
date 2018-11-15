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
    int N,M;
    int baby_leg = 4;
    int old_leg = 3;
    int man_leg = 2;
    cin >> N >> M;
    int man= 0;
    int baby = 0;
    for(int old = 0;old < 2;old++){
        int by_man = man_leg * (N - old);
        if(by_man > M) //最も足の少ない大人ですでに足の合計の上限を超えてしまう場合
            break;
        if((M - by_man - old_leg * old) % (baby_leg - man_leg) == 0) {
            baby = (M - by_man - old_leg * old) / (baby_leg - man_leg);
            man = N - baby - old;
            if (man >= 0){
                printf("%d %d %d\n", man, old, baby);
                return 0;
            }
        }
    }
    printf("-1 -1 -1");
    cout << endl;
    return 0;
}
