//#include <stdio.h>
//void originalPrimeNumberCounter(int num) {
//	int flag[105] = { 0 };
//	for (int i = 2; i <= num; i++) {
//		for (int j = 2; j < i; j++) {
//			if (i % j == 0)
//				flag[i] = 1;
//		}
//		if (flag[i] == 0)
//			printf("%d ", i);
//	}
//}
//int main() {
//	originalPrimeNumberCounter(100);
//	return 0;
//}