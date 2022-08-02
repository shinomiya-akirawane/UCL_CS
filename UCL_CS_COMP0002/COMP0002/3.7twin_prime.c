//#include <stdio.h>
//int primes[1000];
//int dis[1000];
//int len = 2;
//void originalPrimeNumberCounter(int a,int b) {
//		int flag[105] = { 0 };
//		int cnt = 1;
//		for (int i = a; i <= b; i++) {
//			for (int j = 2; j < i; j++) {
//				if (i % j == 0)
//					flag[i] = 1;
//			}
//			if (flag[i] == 0)
//				primes[cnt++] = i;
//		}
//	}
//
//void calDistance() {
//	while (primes[len] != 0) {
//		dis[len] = primes[len] - primes[1];
//		len++;
//	}
//}
//
//void ans() {
//	for (int i = 2; i <= len; i++) {
//		if (dis[i] - dis[i - 1] > dis[i + 1] - dis[i])
//			printf("%d %d\n", primes[i], primes[i+1]);
//		else
//			printf("%d %d\n", primes[i-1], primes[i]);
//	}
//}
//int main() {
//	int a, b;
//	memset(primes, 0, sizeof(primes));
//	scanf("%d %d", &a, &b);
//	originalPrimeNumberCounter(a, b);
//	calDistance();
//	ans();
//	return 0;
//}