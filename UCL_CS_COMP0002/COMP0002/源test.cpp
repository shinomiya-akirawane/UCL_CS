#include<iostream>
#include<cstring>
using namespace std;
char a[1001], b[1001];
long long lena, lenb, i, j, n[10001];
int main()
{
	cin >> a >> b;
	lena = strlen(a);
	lenb = strlen(b);
	for (i = 0; i <= lena - 1; i++) for (j = 0; j <= lenb - 1; j++) n[i + j + 1] += (int(a[i]) - 48) * (int(b[j]) - 48);//诸位相乘保存在对应的位置然后加
	for (i = lena + lenb - 1; i > 1; i--)
		if (n[i] >= 10)
		{
		n[i - 1] += n[i] / 10;
		n[i] %= 10;//处理进位问题
		}
	for (i = 1; i <= lena + lenb - 1; i++) cout << n[i];
	}