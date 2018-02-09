#include <bits/stdc++.h>
using namespace std;
int main()
{
	unsigned long long n,m,x = 1,y;
	cin >> n >> m;
	y = pow(2,n) - 1;
	x = (m&y);
	cout << x << endl;
}
