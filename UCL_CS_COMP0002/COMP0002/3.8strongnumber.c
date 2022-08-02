//#include <stdio.h>
//int calFactorial(int a) {
//	int ans = 1;
//		for (int i = 1; i <= a; i++) {
//			ans = ans * i;
//	}
//	return ans;
//}
//int strongNum(int num) {
//	int dig[1000];
//	int cnt = 1;
//	int ans = 0;
//	int temp = num;
//	while (num!=0) {
//		dig[cnt] = num % 10;
//		num = num / 10;
//		cnt++;
//	}
//	for (int i = 1; i <= cnt; i++) {
//		ans += calFactorial(dig[i]);
//	}
//	if (temp == (ans - 1))
//		return 1;
//}
//int main() {
//	int a, b;
//	scanf("%d %d", &a, &b);
//	for (int i = a; i <= b; i++) {
//		if (strongNum(i) == 1)
//			printf("%d", i);
//	}
//	return 0;
//}