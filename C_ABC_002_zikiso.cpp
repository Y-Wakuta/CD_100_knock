nclude <iostream>

using namespace std;


int main() {
      cin.tie(0);
      ios::sync_with_stdio(false);

      long long a,b,c,d,e,f;
      cin >> a >> b >> c >> d >> e >> f;

      double area = (abs((c - a) * (f - b) - (d - b) * (e - a)) / 2.0);
      cout << fixed << area << endl;
      return 0;
}

