#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

#define REP(i,n) for(int i = 0;i < n;i++)

using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int N,K;
    cin >> N >> K;
    vector<int> R;
    REP(i,N){
        int r = 0;
        cin >> r;
        R.push_back(r);
    }
    sort(R.begin(),R.end());

    double ans = 0;
    for(int i = N - K;i < N;i++)
        ans = (ans + R[i]) / 2.0;

    cout << fixed << ans << endl;

    return 0;
}
