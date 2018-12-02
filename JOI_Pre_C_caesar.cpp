#include <iostream>
#include <vector>
#include <string>
#include <map>
//#include <bits/stdc++.h>

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define ALL(x) (x).begin(),(x).end()

#define DIFF 13

using namespace std;
using ll = long long;
using tp = tuple<ll,ll,ll,ll>;
using P = pair<int,int>;

string get_line(){
    string str="";
    char c;
    while((c=getchar()) != '\n'){
        str += c;
    }
    return str;
}

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);

    //write here
    string str;
    str = get_line();
    map<char,char> dict;
    for(char c = 'A';c <= 'Z';c++){
        char d = '\0';
        if(c + DIFF > 'Z')
            d = c + DIFF - ('Z' - 'A' + 1);
        else d = c + DIFF;
        dict.insert(make_pair(d,c));
    }
    for(char c = 'a';c <= 'z';c++){
        char d = '\0';
        if(c + DIFF > 'z')
            d = c + DIFF - ('z' - 'a' + 1);
        else d = c + DIFF;
        dict.insert(make_pair(d,c));
    }

    string output = "";
    for(auto c: str){
        if(c == ' ')
            output += ' ';
        else if(('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z'))
            output += dict.at(c);
        else output += c;
    }

    cout << output << endl;

    return 0;
}
