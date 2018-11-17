#include <iostream>
#include <vector>
#include <string>
#include <bits/stdc++.h>

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define ALL(x) (x).begin(),(x).end()

using namespace std;
using ll = long long;
using tp = tuple<ll,ll,ll,ll>;
using P = pair<int,int>;

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);

    //write here
    int R,C,sr,sc,gr,gc;
    vector<string> maze;
    string row;
    queue<P> points;

    cin >> R >> C;
    cin >> sr >> sc;
    cin >> gr >> gc;

    //start,goalは1スタートの座標で与えられるのに対して、迷路の座標は0スタートなのでそこを合わせる
    sr--;
    sc--;
    gr--;
    gc--;

    int dist[R][C];
    REP(r,R)
        REP(c,C)
            dist[r][c] = -1;

    REP(i,R){
        cin >> row;
        maze.push_back(row);
    }
    points.push(make_pair(sr,sc));
    dist[sr][sc] = 0;

    while(!points.empty()) {
        P point = points.front();
        points.pop();
        for (int r = -1; r < 2; r++) {
            for (int c = -1; c < 2; c++) {
                if(r == c == 1 || r== c== -1 || r + c ==0)//斜め飛び防止
                    continue;
                int dr = point.first + r;
                int dc = point.second + c;
                if (0 <= dr && dr < R && 0 <= dc && dc < C && maze[dr][dc] == '.' && dist[dr][dc] == -1) {
                    dist[dr][dc] = dist[point.first][point.second] + 1;
                    points.push(make_pair(dr, dc));
                }
            }
        }
    }

    printf("%d\n",dist[gr][gc]);

    return 0;
}
